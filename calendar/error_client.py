import grpc
from grpcError import error_pb2, error_pb2_grpc
import logging

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = error_pb2_grpc.ErrorMethodStub(channel)
        print('----- SendError -----')
        response = stub.SendErrot(error_pb2.AddError(id=131, flag=False))
        
        print(response, end='')


if __name__ == '__main__':
    logging.basicConfig()
    run()
