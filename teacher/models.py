from django.db import models
from django.contrib.auth.models import User
import uuid
from mother.models import Child
from django.db.models.signals import post_save
from django.dispatch import receiver


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)

class Report(models.Model):

    child = models.ForeignKey(Child,on_delete=models.CASCADE,null=True,blank=True)
    text = models.TextField(max_length=2000, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    # created = models.DateTimeField(auto_now_add=True,editable=False)
    def __str__(self):
        return str(self.text)

    # def __str__(self):
    #     return str(self.created)
