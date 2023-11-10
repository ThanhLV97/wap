from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Action, DataIngestion, Model
from .serializers import (ActionSerializer, DataIngestionSerializer,
                          ModelSerializer)


class ModelViewSet(APIView):

    def get(self, request):
        items = Model.objects.all()
        serializer = ModelSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModelDetailViewSet(APIView):

    def get_object(self, pk):
        try:
            return Model.objects.get(pk=pk)
        except Model.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        model = self.get_object(pk)
        serializer = ModelSerializer(model)
        return Response(serializer.data)

    def put(self, request, pk):
        model = self.get_object(pk)
        serializer = ModelSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model = self.get_object(pk)
        model.is_deleted = True
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DataIngestionList(APIView):

    def get(self, request):
        files = DataIngestion.objects.all()
        serializer = DataIngestionSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataIngestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataIngestionDetail(APIView):

    def get_object(self, pk):
        try:
            return DataIngestion.objects.get(pk=pk)
        except DataIngestion.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        file = self.get_object(pk)
        serializer = DataIngestionSerializer(file)
        return Response(serializer.data)

    def put(self, request, pk):
        file = self.get_object(pk)
        serializer = DataIngestionSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        file = self.get_object(pk)
        file.is_deleted = True
        file.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActionViewSet(APIView):

    def get(self, request):
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActionDetailViewSet(APIView):

    def get(self, request, pk):
        action = self.get_object(pk)
        serializer = ActionSerializer(action)
        return Response(serializer.data)

    def put(self, request, pk):
        action = self.get_object(pk)
        serializer = ActionSerializer(action, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        action = self.get_object(pk)
        action.is_deleted = True
        action.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
