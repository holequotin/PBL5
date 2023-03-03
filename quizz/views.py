from django.shortcuts import render,redirect
from .forms import *
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
            form.save()
            return redirect('quizz:Login')
    else:
        form = RegisterForm()
    context = {
        'title' : 'Register',
        'form' : form,
    }
    return render(request,'register.html',context)