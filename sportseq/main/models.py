from tkinter import CASCADE
from xmlrpc.client import Boolean
from django.db import models
from numpy import roll, true_divide

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    rollNo = models.IntegerField(unique=True, primary_key=True)

    def __str__(self):
        return self.name


class SportItem(models.Model):
    name = models.CharField(max_length=200)
    isBorrowed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, to_field="rollNo", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
