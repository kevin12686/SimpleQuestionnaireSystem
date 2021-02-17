from django.db import models


# Create your models here.


class Question(models.Model):
    dp_txt = models.TextField(verbose_name='Content')
    des = models.TextField(blank=True, verbose_name='Description')
    audio = models.FileField(blank=True, upload_to='audio/', verbose_name='Audio')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='Answers')
    dp_txt = models.TextField(verbose_name='Content')
    correct = models.BooleanField(default=False, verbose_name='Correct')


class Respondent(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    mail = models.EmailField(verbose_name='Mail')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')


class Record(models.Model):
    response = models.ForeignKey(Respondent, on_delete=models.CASCADE, related_name='Records', verbose_name='Response')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='Records', verbose_name='Question')
    answers = models.ManyToManyField(Answer, related_name='Records', verbose_name='Selected Answers')
    correct = models.BooleanField(default=False, verbose_name='Correct')
