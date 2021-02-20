from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from cart.models import PaidOrder


class NewUser(AbstractUser):
    username = models.CharField('username', max_length=50, unique=True)
    email = models.EmailField('email', max_length=254, unique=True)
    password = models.CharField('password', max_length=50)
    catalog = models.ManyToManyField(PaidOrder, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
