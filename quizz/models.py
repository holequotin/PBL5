from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
# Create your models here.

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Role(models.Model):
    name = models.CharField(unique=True,max_length=100)
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

class Level(models.Model):
    name =  models.CharField(unique=True,max_length=100)
    
    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(unique=True,max_length=100)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',default='media/default.jpeg',storage=fs)
    pass_score = models.IntegerField(default=0)
    
    def parts(self):
        return ExamPart.objects.all().filter(exam = self)
    
    def get_detail(self):
        return reverse('quizz:ExamDetail', kwargs={'pk' : self.id})
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        return super().delete(*args, **kwargs)
    
    
class ExamPart(models.Model):
    name = models.CharField(max_length=100)
    time = models.PositiveIntegerField()
    pass_score = models.PositiveIntegerField(default=0)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    
    def groups(self):
        return GroupQuestion.objects.all().filter(exam_part = self)

class GroupQuestion(models.Model):
    exam_part = models.ForeignKey(ExamPart,on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/',null=True, blank=True)
    
    def questions(self):
        return Question.objects.all().filter(group_question = self)
    
class Question(models.Model):
    group_question = models.ForeignKey(GroupQuestion, on_delete= models.CASCADE)
    content = models.CharField(max_length=1000)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    score = models.IntegerField()
    correct = models.CharField(max_length=1,default="A")

class PracticeHistory(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now_add=True)
    score = models.IntegerField()
    status = models.CharField(max_length=100)

class PracticePartHistory(models.Model):
    name = models.CharField(max_length=100)
    time = models.DurationField()
    pass_score = models.IntegerField(default=0)
    practice_history = models.ForeignKey(PracticeHistory,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    time_left = models.DurationField()
    
class GroupQuestionHistory(models.Model):
    practice_part_history = models.ForeignKey(PracticePartHistory,on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/')
    
class QuestionHistory(models.Model):
    group_question_history = models.ForeignKey(GroupQuestionHistory,on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    score = models.IntegerField()
    correct = models.CharField(max_length=1)
    answer = models.CharField(max_length=1)