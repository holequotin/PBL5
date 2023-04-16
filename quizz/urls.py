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
    path('examdetail/<int:pk>/',exam_detail,name='ExamDetail'),
    
    path('htmx-add-exam-form',add_exam_form,name='AddExamForm'),
    path('htmx-add-exam-part-form/<int:pk>/',add_part_form, name = "AddExamPartForm"),
    path('htmx-detail-exam-part/<int:pk>/',detail_exam_part,name='DetailExamPart'),
    path('htmx-group-question-form/<int:pk>/',group_question_form,name="GroupQuestionForm"),
    path("htmx-question-form/<int:pk>/", add_question_form , name="AddQuestionForm"),
    
    path('htmx-delete-question/<int:pk>/',delete_question,name='DeleteQuestion'),
    path("htmx-detail-question/<int:pk>", detail_question, name="DetailQuestion"),
    path("htmx-delete-form/", delete_form, name="DeleteForm"),
    path("htmx-delete-part/<int:pk>/",delete_part,name='DeletePart'),
    path('htmx-delete-group/<int:pk>/',delete_group,name = 'DeleteGroup')
]
