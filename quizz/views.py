from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
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
    return render(request,'pages/landing_page.html',{})

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
    return render(request,'pages/login.html',context)

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
    return render(request,'pages/teacher.html',context)

@login_required(login_url='quizz:Login')
@user_passes_test(is_teacher,'quizz:Login','quizz:AddExam')
def add_exam_view(request):
    if request.method == "POST":
        form = AddExamForm(request.POST,request.FILES)
        print(form.data)
        if form.is_valid():
            exam =  form.save(commit=False)
            exam.user = request.user
            exam.save()
            return redirect('quizz:ExamDetail',pk = exam.id)
        # else:
        #     print('Invalid')
        #     return render(request,'part/add_exam_form.html',{'form' : form})
    else:
        form = AddExamForm()
    context = {
        'title' : 'Add Exam',
        'form' : form
    }
    return render(request,'pages/add_exam.html',context)

def add_exam_form(request):
    return render(request,'part/add_exam_form.html',{})

def exam_detail(request,pk):
    exam = Exam.objects.get(id = pk)
    form = AddExamForm(instance=exam)
    return render(request,'pages/exam_detail.html',{'form' : form})

def add_part_form(request,pk):
    # print("oke")
    # form = AddExamPartForm(request.POST or None)
    # return render(request,'part/add_exam_part.html',{'form' : form})
    exam = Exam.objects.get(id = pk)
    form = AddExamPartForm(request.POST or None)
    if request.method == "POST":
        print("Hello")
        if form.is_valid():
            exam_part = form.save(commit=False)
            exam_part.exam = exam
            exam_part.save()
            return redirect('quizz:DetailExamPart',pk = exam_part.id)
        else:
            print("Error")
            return HttpResponse("Error")
    
    return render(request,'part/add_exam_part.html',{'form' : form,'exam' : exam})    

def detail_exam_part(request,pk):
    exam_part = ExamPart.objects.get(id = pk)
    return render(request,'part/detail_exam_part.html',{'part' : exam_part,'pk' : pk})

def group_question_form(request,pk):
    form = AddGroupQuesitonForm(request.POST or None)
    if request.method == "POST" :
        form = AddGroupQuesitonForm(request.POST or None,request.FILES)
        if form.is_valid():
            print('Group Question is valid')
            group_question = form.save(commit=False)
            part = get_object_or_404(ExamPart,id = pk)
            print(part)
            group_question.exam_part = part
            group_question.save()                                                                                                                                                                                                                                                   
            return render(request,'part/detail_group_question.html',{'group' : group_question})
    return render(request,'part/group_question_form.html', {'form' : form,'part_id' : pk})

def add_question_form(request,pk):
    if request.method == "POST":
        print("POST")
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            group_question = get_object_or_404(GroupQuestion,id = pk)
            question.group_question = group_question
            question.save()
            return redirect('quizz:DetailQuestion', pk = question.id)
        else:
            print("Is not valid")
    form = AddQuestionForm()
    return render(request,'part/question_form.html',{'form' : form , "pk" : pk})
def delete_question(request,pk):
    question = get_object_or_404(Question,id = pk)
    question.delete()
    return HttpResponse('')

def detail_question(request,pk):
    question = get_object_or_404(Question,id = pk)
    return render(request,'part/detail_question.html',{'question' : question })

def delete_form(request):
    return HttpResponse('')

def delete_part(request,pk):
    part = get_object_or_404(ExamPart,id = pk)
    part.delete()
    return HttpResponse('')

def delete_group(request,pk):
    group = get_object_or_404(GroupQuestion,id=pk)
    group.delete()
    return HttpResponse('')