from django.shortcuts import render

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
    context = {
        'title' : 'Register'
    }
    return render(request,'register.html',context)