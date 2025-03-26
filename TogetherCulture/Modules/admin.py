from django.contrib import admin

# Register your models here.
from django.contrib import admin


# Register your models here.
from .models import Venue, Module, MyClubUser, Booking   

admin.site.register(Venue)  
admin.site.register(Module)
admin.site.register(MyClubUser)
admin.site.register(Booking)

