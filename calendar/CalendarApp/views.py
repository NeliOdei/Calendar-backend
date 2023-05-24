from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
import jwt
from requests import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from CalendarApp.models import User, Tasks, Types, Colors, TasksFilter, AddError
from rest_framework import viewsets, generics
from CalendarApp.serializers import UsersSerializer, TasksSerializer, TypesSerializer, ColorsSerializer, PostProtoSerializer
from rest_framework.decorators import api_view
import grpc;
from gRPC import calendar_pb2
from dateutil.parser import parse
import datetime

from google.protobuf import empty_pb2
from django_grpc_framework.services import Service


from django.http import HttpResponse

from django.http import JsonResponse

from gRPC.calendar_pb2 import AddNote
import gRPC.client
import gRPC.calendar_pb2
import grpcError.error_pb2
from grpcError import error_pb2

from gRPC.calendar_pb2_grpc import CalendarServiceStub



   
   

class ColorsViewSet(viewsets.ModelViewSet):
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TasksFilter
    permission_classes = [IsAuthenticated]


class TaskFilterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_serializer(self, *args, **kwargs):
        serializer_class = TasksSerializer
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):

        fromDate = self.request.query_params.get('fromDate',None)
        toDate = self.request.query_params.get('toDate',None)
        response  = Tasks.objects.filter(dateTask__gte=fromDate,dateTask__lte=toDate)
        permission_classes = [IsAuthenticated]
        return response


@api_view(['POST'])
def test(request: Request):

    form = TasksSerializer(data=request.data)
    if form.is_valid():
        form.save()

    user = User.objects.filter(pk=form.data['user'])
    serializertask = UsersSerializer(user, many=True)
    # serializerusers = UsersSerializer(data=user, many=True)
    # serializerusers.is_valid(raise_exception=True)
    #     email = serializerusers.data['email']


    my_request = AddNote(
        id=form.data['pk'],
        note=form.data['tname'],
        date_note= form.data['dateTask'],
        date_remind=form.data['datenotif'],
        email= serializertask.data[0]['email']
    )

    try:

        channel = grpc.insecure_channel('localhost:60051')
        my_stub = CalendarServiceStub(channel)
        response = my_stub.RecieveData(my_request)


        # Возвращаем ответ в виде JSON
    #     return JsonResponse(my_response)
    except grpc.RpcError as e:
        # Обрабатываем ошибку
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            return HttpResponse('Сервер недоступен', status=500)
        else:
            return HttpResponse(str(e), status=500)

    return Response({'success': response.status});
    # return Response({'success': serializertask.data[0]['email']});


    


@api_view()
def user(request: Request):
    return Response({
        'data': UsersSerializer(request.user).data
    })
# Create your views here.



class ErrorService(Service):
#    def get_object(self, pk):
#     try:
#         note = Task.objects.filter(pk=pk)
        
#         return note
#     except Tasks.DoesNotExist:
#         self.context.abort(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % pk)

   def SendErrot(self, request, context):
        print('New request: Add error')
        # task = self.get_object(request.id)
        # serializertask = TasksSerializer(task, many=True)
        # print("before", serializertask.data[0]['email'])
        # serializertask.data[0]['flag']=False
        # print("flag", serializertask.data[0]['flag'])
        try:
            task = Tasks.objects.filter(pk=request.id).update(flag=False)
            status = error_pb2.Status(status=True)
            print("flag: False")
        except:
            status = error_pb2.Status(status=False)
            print("error")

        # serializertask = TasksSerializer(task, many=True)
       
        # serializertask = TasksSerializer(data= serializertask.data)
        # serializertask.is_valid(raise_exception=True)
        # serializertask.save()
        
        # serializer = PostProtoSerializer(message=request)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        
        
       
        return status
