# Serializers
from django_socio_grpc import proto_serializers
from rest_framework import serializers

from .models import Action, CustomUser, DataIngestion, Model, UploadedFile


class ModelProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = Model
        fields = ['id', 'name', 'version', 'updated_at']


class DataIngestionProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = DataIngestion
        fields = ['id', 'name', 'file', 'description', 'uploaded_at']


class UploadedFileProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = UploadedFile
        fields = ['id', 'title', 'file', 'created_at', 'updated_at']

import apis.grpc.apis_pb2 as apis_pb2


class CustomUserProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = CustomUser
        proto_class = apis_pb2.CustomUserResponse
        proto_class_list = apis_pb2.CustomUserListResponse # Modification here

        fields = ['id', 'email', 'is_active']


class AuthProtoSerializer(proto_serializers.ProtoSerializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.EmailField(max_length=100)

    class Meta:
        model = CustomUser
        proto_class = apis_pb2.AuthRequest
        proto_class_list = apis_pb2.AuthResponse


class ActionProtoSerializer(proto_serializers.ModelProtoSerializer):
    model_id = serializers.IntegerField()

    class Meta:
        model = Action
        proto_class = apis_pb2.ActionRequest
        proto_class_list = apis_pb2.ActionListResponse # Modification here

        fields = ['id', 'model_id', 'action_type', 'status']
