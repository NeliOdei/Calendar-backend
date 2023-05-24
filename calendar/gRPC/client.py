import logging

import grpc
from gRPC import calendar_pb2
from gRPC import calendar_pb2_grpc





# def test_add_notion(stub, request):
#     status = stub.RecieveData(request)
#     print(status.status)
    


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # with grpc.insecure_channel('localhost:50051') as channel:

    #     global stub
    #     stub = calendar_pb2_grpc.CalendarServiceStub(channel)
        global stub
        stub = calendar_pb2_grpc.CalendarServiceStub(grpc.insecure_channel('localhost:50051'))
        print(stub)
        print("-------------- AddNotion --------------")
        # test_add_notion(stub, calendar_pb2.AddNote(id=1, note='Театр', date_note='2023-05-15T21:00:00Z', date_remind='2023-05-15T21:00:00Z',email='Yurova_evg@mail.ru'))
       
        channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    run()
