from django.db import models

# Create your models here.


class Pets(models.Model):
    pid = models.IntegerField(primary_key=True)
    petname = models.CharField(max_length=50)
    age = models.IntegerField(default=None)
    description = models.TextField(default=None)


class Books(models.Model):
    bookid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default=None)
    price = models.FloatField()
