from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    country = models.CharField(max_length=300)

class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    sex = models.CharField(max_length=10)
    tel = models.CharField(max_length=12)
    member_in = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Book(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)