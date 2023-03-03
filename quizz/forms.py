from django.forms import models
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control", 
        "id" : "firstname",
        "name" : "firstname",
        "placeholder" : "Họ"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control", 
        "id" : "lastname",
        "name" : "lastname",
        "placeholder" : "Tên"
    }))
    # email = forms.CharField(widget=forms.TextInput(attrs={
    #     "class":"form-control",
    #     "id":"email",
    #     "name" : "email",
    #     "placeholder" : "Email"
    # }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "id" : "password1",
        "name" : "password1",
        "placeholder" : "Mật khẩu"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "id" : "password2",
        "name" : "password2",
        "placeholder" : "Xác nhận mật khẩu"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-control",
        "id" : "username",
        "name" : "username",
        "placeholder" : "Tên đăng nhập"
    }))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2