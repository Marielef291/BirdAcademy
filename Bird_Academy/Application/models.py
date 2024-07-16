from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bird (models.Model):
    Latin_name =models.CharField(max_length=100)
    Fr_name =models.CharField(max_length=100, null= True, blank=True)
    Eng_name =models.CharField(max_length=100,null= True, blank=True)
    User_Bird = models.ManyToManyField(User,related_name = 'birds', blank=True)
    
class Song (models.Model) :
    URL_Song = models.CharField(max_length=100)
    List_Other_Birds = models.CharField(max_length=100, blank=True)
    Id_bird = models.ForeignKey(Bird, on_delete=models.CASCADE)