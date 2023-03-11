from django.urls import path,include
from .views import *\

app_name = 'quizz'
urlpatterns = [
    path('',landing_view,name = 'LandingPage'),
    path('login/',login_view,name='Login'),
    path('register/',register_view,name='Register'),
    path('home/',student_view,name = 'Home'),
    path('logout/',logout_view,name = 'Logout'),
    path('teacher/',teacher_view,name = 'TeacherPage'),
    path('addexam/',add_exam_view,name = 'AddExam'),
]
