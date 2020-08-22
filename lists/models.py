from django.db import models

# Create your models here.


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(max_length=100, default='')
    list = models.ForeignKey(List, default='')
