# apis/services.py
import datetime

import grpc
import jwt
from asgiref.sync import sync_to_async
from django_socio_grpc import generics

import apis.grpc.apis_pb2 as apis_pb2
from wowai.settings import JWT_SECRET, TOKEN_EXPIRATION

from .grpc_serializers import AuthProtoSerializer, CustomUserProtoSerializer
from .models import CustomUser

########################################################################################################################
#                                                 USER SERVICE
########################################################################################################################

class CustomUserService(generics.AsyncModelService):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserProtoSerializer


########################################################################################################################
#                                                 AUTH SERVICE
########################################################################################################################

class AuthenService(generics.CreateService):
    serializer_class = AuthProtoSerializer

    async def Create(self, request, context):
        "Token generation"
        try:
            response = apis_pb2.AuthResponse()

            email = request.email
            password = request.password

            user = await sync_to_async(CustomUser.objects.get)(email=email)
            valid = user.check_password(password)

            if valid:
                token = generate_token(user)
                response.token = token

            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED.name

            return response

        except Exception:
            return grpc.StatusCode.UNAUTHENTICATED


def generate_token(user):
    """Generate token from user."""
    payload = {
        'user_info': {
            'username': user.username,
            'email': None,
            'is_superuser': user.is_superuser,
            'user_id': user.id
        },
        'exp': datetime.datetime.utcnow() +  datetime.timedelta(hours=TOKEN_EXPIRATION)
    }

    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')
