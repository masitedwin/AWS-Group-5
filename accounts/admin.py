

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ApprovedUser  # to import the  ApprovedMember models

# Custom action to approve users
def approve_users(modeladmin, request, queryset):
    for user in queryset:
        if not user.is_active:  # to check if the user is not already approved
            user.is_active = True  # to set the user as active
            user.save()

            # to send an email to the user notifying them of approval
            send_mail( 
                subject='Your account has been approved',
                message=f'Hello {user.first_name}, \n\nCongratulations! Your account has been approved. You can now Log in.',
                from_email= 'dickyrono@gmail.com',
                recipient_list=[user.email],
                fail_silently=False,
            )
    
approve_users.short_description = "Approve selected users"

# this is the approved Members Section
@admin.register(ApprovedUser)
class ApprovedUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name', 'email', 'is_staff')
    ordering = ('first_name','email')
    
    search_fields = ('first_name', 'last_name', 'email')

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_active=True)  # this show only the approved users

class UserAdmin(BaseUserAdmin):
    list_display = ('username','first_name', 'email', 'is_staff', 'is_active')  # to show list of user information on admins page
    list_filter = ('is_active', 'is_staff')  # filter by approval status
    actions = [approve_users] # approval button
    

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('is_active')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
