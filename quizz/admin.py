from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Level)
admin.site.register(Exam)
admin.site.register(ExamPart)
admin.site.register(GroupQuestion)
admin.site.register(Question)
admin.site.register(PracticeHistory)
admin.site.register(PracticePartHistory)
admin.site.register(GroupQuestionHistory)
admin.site.register(QuestionHistory)