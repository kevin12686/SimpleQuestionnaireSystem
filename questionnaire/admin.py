from django.contrib import admin
from .models import Question, Answer, Respondent, Record

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Respondent)
admin.site.register(Record)
