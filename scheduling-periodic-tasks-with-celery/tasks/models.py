from django.db import models


# Create your models here.
class UserInstance(models.Model):
    name = models.CharField(max_length=10)
    time = models.DateTimeField()