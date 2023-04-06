from django.forms import models
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from durationwidget.widgets import TimeDurationWidget

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

class AddExamForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control col-6',
        'id' : 'exam-name',
        'name' : 'exam-name'
    }))
    level = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class' : 'form-control',
        'id' : 'exam-level',
        'name' : 'exam-level'
    }),queryset=Level.objects.all())
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'form-control',
        'id' : 'exam-image',
        'name' : 'exam-image'
    }))
    pass_score = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'id' : 'exam-pass-score',
        'name' : 'exam-pass-score'
    }))
    class Meta:
        model = Exam
        fields = ['name','level','image','pass_score']
        
class AddExamPartForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
    }))
    time = forms.IntegerField(widget = forms.NumberInput(attrs={
        'class' : 'form-control',
    }))
    pass_score = forms.IntegerField(widget = forms.NumberInput(attrs={
        'class' : 'form-control',
        'min' : 0
    }))
    class Meta:
        model = ExamPart
        fields = ['name','time','pass_score']
        
class AddGroupQuesitonForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class' : 'form-control'
    }),required=False)
    class Meta:
        model = GroupQuestion
        fields = ['content','file']