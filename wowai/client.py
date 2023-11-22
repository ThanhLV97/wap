import grpc

import apis.grpc.apis_pb2 as apis_pb2
import apis.grpc.apis_pb2_grpc as apis_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:

    auth_stub = apis_pb2_grpc.AuthenControllerStub(channel)
    response = auth_stub.Create(request=apis_pb2.AuthRequest(email='dev@gmail.com', password='1'))
    print(response.token or response.status)
