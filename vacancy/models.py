from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, related_name='resume', on_delete=models.CASCADE)
