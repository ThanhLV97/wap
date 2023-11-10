# Serializers
from rest_framework import serializers

from .models import Action, DataIngestion, Model


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ['id', 'name', 'version', 'updated_at']


class DataIngestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataIngestion
        fields = ['id', 'name', 'file', 'description', 'uploaded_at']


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ['id', 'name', 'description', 'updated_at']
