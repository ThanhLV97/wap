# Models Defination

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.model import BaseModel, ModelManager


class Model(BaseModel):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    objects = ModelManager()

    def __str__(self) -> str:
        return str(self.name)


class UploadedFile(BaseModel):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')


class DataIngestion(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    objects = ModelManager()

    def __str__(self) -> str:
        return str(self.name)


class Action(BaseModel):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    objects = ModelManager()

    def __str__(self) -> str:
        return str(self.action_type)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """Customized user model which replace username field with email."""

    username = None
    email = models.EmailField(_("Email address"), unique=True)

    # Define unique identifier for user to email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Set all object for this class come from CustomerUserManager
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
