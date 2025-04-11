from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class benefits(models.Model):  
    benefits = models.CharField('Benefits', max_length=120)
      

def __str__(self):
    return self.benefits