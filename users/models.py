from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    vrf_token = models.CharField(max_length=12, verbose_name='токен', **NULLABLE)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []