# Generated by Django 4.1.7 on 2023-03-30 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0006_exam_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='time',
        ),
    ]
