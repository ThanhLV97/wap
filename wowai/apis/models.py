# Models Defination

from core.model import BaseModel, ModelManager
from django.db import models


class Model(BaseModel):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    objects = ModelManager()

    def __str__(self):
        return self.name


class DataIngestion(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    objects = ModelManager()

    def __str__(self):
        return self.name


class Action(BaseModel):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    objects = ModelManager()

    def __str__(self):
        return self.action_type
