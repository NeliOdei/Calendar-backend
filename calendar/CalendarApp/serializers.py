from rest_framework import serializers

from CalendarApp.models import Tasks
from CalendarApp.models import Colors
from CalendarApp.models import Types, AddError
from django.contrib.auth.models import User
from django_grpc_framework import proto_serializers
from grpcError import error_pb2

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "password", "is_staff", 'email']


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ["pk", "tname", "descr", "dateTask", "color", "type", "datenotif", "reminder", "user", "flag"]


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ["pk", "color"]


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ["pk", "type"]


class PostProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = AddError
        proto_class = error_pb2.AddError
        fields = ['pk', 'flag']



