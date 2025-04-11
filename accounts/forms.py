from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postcode = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'postcode', 'password1', 'password2')
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = False  # this is for approval process, the user is not active until approved

        if commit:
            user.save()
        return user
        
class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postcode = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))

class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'address', 'postcode')
   
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
    self.fields['email'].widget.attrs.update({'class': 'form-control'})
    self.fields['address'].widget.attrs.update({'class': 'form-control'})
    self.fields['postcode'].widget.attrs.update({'class': 'form-control'})