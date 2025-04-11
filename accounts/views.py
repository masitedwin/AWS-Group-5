from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login ,authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from.forms import RegisterUserForm, UpdateUserForm
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login, authenticate



def home_view(request):
    return render(request, 'home.html')

# views are shown here
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        
        if user_form.is_valid():
            user_form.save()
              
            user = authenticate(username = current_user.username, password = request.POST.get('password'))
            # If the user is authenticated, log them in again
           

            if user:
                login(request, user)

            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('home')
        
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, "You Must Be Logged in to Access that Page")
        return redirect('login')
    
# User Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. Please wait for approval.')
            form = RegisterUserForm()  # Reset the form after successful registration
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})

def user_login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()

            if user is not None:
                if user.is_superuser or user.is_staff:
                    messages.error(request, 'Admin must log in through the admin site.')
                    return redirect('custom_login')

                if not user.is_active:
                    messages.error(request, 'Your account is not active. Please wait for approval.')
                    return redirect('login')

                login(request, user)
                messages.success(request, 'You have logged in successfully.')
                return redirect('dashboard')

            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

class CustomAdminLoginView(LoginView):
    template_name = 'custom_login.html'  # the path to your custom admin login template

    def get_success_url(self):
        return reverse_lazy('admin:index')  # Redirect to the inbuilt admin  page after successful login

    def form_valid(self, form):
        
        return super().form_valid(form)  # Call the parent class's form_valid method to proceed with login