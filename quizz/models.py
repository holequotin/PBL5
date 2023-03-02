from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
    name = models.CharField(unique=True,max_length=100)
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

class Level(models.Model):
    name =  models.CharField(unique=True,max_length=100)

class Exam(models.Model):
    name = models.CharField(unique=True,max_length=100)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    duration = models.DurationField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class ExamDetail(models.Model):
    content = models.TextField()
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    correct = models.CharField(max_length=1)
    exam = models.OneToOneField(Exam,on_delete=models.CASCADE)

class Practice(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    time_start = models.TimeField(auto_now=False, auto_now_add=True)
    time_left = models.DurationField()
    score = models.DecimalField(decimal_places=2,max_digits=4)
    
class CompletePractice(models.Model):
    practice = models.ForeignKey(Practice,on_delete=models.CASCADE)
    exam_detail = models.ForeignKey(ExamDetail,on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)

class TakeATest(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher')
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student')
    time_start = models.TimeField(auto_now=False, auto_now_add=True)
    time_left = models.DurationField()
    score = models.DecimalField(decimal_places=2,max_digits=4)
    
class CompleteTest(models.Model):
    take_test = models.ForeignKey(TakeATest,on_delete=models.CASCADE)
    exam_detail = models.ForeignKey(ExamDetail,on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)