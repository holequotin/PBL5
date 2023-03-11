from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def is_student(user):
    if user is not None:
        print(user)
        profile = Profile.objects.get(user = user)
        if profile is not None:
            role = Role.objects.get(id = 2)
            if role == profile.role:
                return True
    return False

def is_teacher(user):
    if user is not None:
        print(user)
        profile = Profile.objects.get(user = user)
        if profile is not None:
            role = Role.objects.get(id = 1)
            if role == profile.role:
                return True
    return False
    
def landing_view(request):
    context = {
        'title' : 'Trang chủ'
    }
    return render(request,'landing_page.html',{})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]
        user = authenticate(username = username,password = password)     
        if user is not None:
            login(request,user)
            if role == "student":
                return redirect('quizz:Home')
            elif role == "teacher":
                return redirect('quizz:TeacherPage')

    context = {
        'title' : 'Đăng nhập'
    }
    return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('quizz:LandingPage')

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

@login_required(login_url='quizz:Login')
@user_passes_test(is_student,'quizz:Login','quizz:Home')
def student_view(request):
    return render(request,'student.html',{'title' : 'Home'})


@login_required(login_url='quizz:Login')
@user_passes_test(is_teacher,'quizz:Login')
def teacher_view(request):
    exams = Exam.objects.all()
    context = {
        'title' : 'Teacher Page',
        'exams' : exams
    }
    return render(request,'teacher.html',context)

@login_required(login_url='quizz:Login')
@user_passes_test(is_teacher,'quizz:Login','quizz:AddExam')
def add_exam_view(request):
    if request.method == "POST":
        form = AddExamForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quizz:TeacherPage')
    else:
        form = AddExamForm()
    context = {
        'title' : 'Add Exam',
        'form' : form
    }
    return render(request,'add_exam.html',context)
