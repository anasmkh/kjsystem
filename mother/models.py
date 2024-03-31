from django.db import models
from django.contrib.auth.models import User
# from teacher.models import Teacher,Report
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save

class Mother(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)

class Child(models.Model):
    meal_types = (('meat', 'Meat'),
                  ('milk', 'milk'))
    gender = (
        ('male','Male'),
        ('female','Female')
    )
    mom = models.ForeignKey(Mother,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True,blank=True)
    age = models.CharField(max_length=200,null=True,blank=True)
    child_gender = models.CharField(max_length=200, null=True, blank=True, choices=gender)
    featured_image = models.ImageField(null=True,blank=True,upload_to='staticfiles/images/',default='default.png')
    meal = models.CharField(max_length=200, null=True, blank=True, choices=meal_types)
    notes = models.CharField(max_length=200,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


