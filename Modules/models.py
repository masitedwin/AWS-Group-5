from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip/Post Code', max_length=12)
    phone = models.CharField('Contact Phone', max_length=20, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)   

def __str__(self):
    return self.name          
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)     
    email = models.EmailField('User Email') 

def __str__(self):
    return self.first_name + ' ' + self.last_name   

class Module(models.Model):
    name = models.CharField('Module Name' , max_length=120)
    course_date = models.DateTimeField('Course Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)    
    #venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, through='Booking', blank=True)

def __str__(self):
    return self.name



class Booking(models.Model):    
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    customer = models.ForeignKey(MyClubUser, on_delete=models.CASCADE)
    booking_date = models.DateTimeField('Booking Date')
    guest_num = models.PositiveSmallIntegerField('Number of Guests')
    notes = models.TextField('Booking Notes', blank=True)   

def __str__(self):
    return self.event.name + ' ' + self.customer.first_name + ' ' + self.customer.last_name + ' ' + str(self.booking_date) + ' ' + str(self.guest_num) + ' ' + self.notes
# Create your models here.
