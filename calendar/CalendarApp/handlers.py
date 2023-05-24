from CalendarApp.views import ErrorService
from grpcError import error_pb2_grpc


def grpc_handlers(server):
    print('---------AddEror---------')
    error_pb2_grpc.add_ErrorMethodServicer_to_server(ErrorService.as_servicer(), server)