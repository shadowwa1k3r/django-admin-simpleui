from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'
