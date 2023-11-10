from django.db import models


class BaseModel(models.Model):
    """This is base model contained audit fields"""
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        abstract = True


class ModelManager(models.Manager):
    """TODO"""
    def get_queryset(self):
        """Overwrite method for getting record which is not deleted"""
        return super().get_queryset().filter(is_deleted=False)
