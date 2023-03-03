from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def landing_view(request):
    context = {
        'title' : 'Trang chủ'
    }
    return render(request,'landing_page.html',{})

def login_view(request):
    context = {
        'title' : 'Đăng nhập'
    }
    return render(request,'login.html',context)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            role = Role.objects.get(id = 2)
            profile = Profile.objects.create(user = user, role = role)
            profile.save()
            return redirect('quizz:Login')
    else:
        form = RegisterForm()
    context = {
        'title' : 'Register',
        'form' : form,
    }
    return render(request,'register.html',context)