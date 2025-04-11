from django.urls import path, include
from . import views
from .views import CustomAdminLoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns =[
path('register/', views.register, name='register'),
path('login/', views.user_login_view, name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
path('update_user/', views.update_user, name='update_user'),
path('register_success/', TemplateView.as_view(template_name='register_successful.html'), name='register_success'),
path('custom-login/', CustomAdminLoginView.as_view(), name='custom_login'),
path ('',views.home_view, name='home'),
]
