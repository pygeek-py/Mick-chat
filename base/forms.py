from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import message

class registerform(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    
    class Meta():
        model = User
        fields = ["username", "phone", "email", "password1", "password2"]
        
class messageform(forms.ModelForm):
    class Meta:
        model = message
        fields = ["body"]
