from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Submission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    marks = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
