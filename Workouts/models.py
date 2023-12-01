from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
User = get_user_model()
# Create your models here.
class Workout(models.Model):
  title = models.CharField(max_length=100)
  Time = models.CharField(max_length=30,default=0,blank=True,null=True)
  workcount = models.CharField(max_length=30,blank=True,null=True)

  def __str__(self):
    return self.title
  
  def category_count(self):
        return Category.objects.filter(Workout=self).count()

Muscle_types = (("Chest","Chest"),("Biceps","Biceps"),("Triceps","Triceps"),("Legs","Legs"),("Shoulder","Shoulder"),("Back","Back"),("Abs","Abs"),("Cardio","Cardio"))
class Category(models.Model):
  Workout = models.ManyToManyField(Workout,related_name="workout_cat")
  Workout_name = models.CharField(max_length=100)
  Muscle_group = models.CharField(choices=Muscle_types,max_length=100)
  Rep1 = models.IntegerField(default=0)
  Weight1 = models.IntegerField(default=0)
  Rep2 = models.IntegerField(default=0)
  Weight2 = models.IntegerField(default=0)
  Rep3 = models.IntegerField(default=0)
  Weight3 = models.IntegerField(default=0)
  C_time = models.CharField(max_length=30,blank=True,null=True)
  def __str__(self):
    return self.Workout_name





