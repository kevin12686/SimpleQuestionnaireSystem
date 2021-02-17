from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Question, Respondent, Record
import json


# Create your views here.

class QuestionView(TemplateView):
    template_name = 'questionnaire.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            try:
                data = json.loads(request.body)
                rsd = Respondent.objects.create(name=data['name'], mail=data['mail'], phone=data['phone'])
                correct = 0
                total = 0
                for each in data['ans']:
                    rec = Record.objects.create(response=rsd, question_id=each['qid'])
                    rec.answers.add(each['ans'])
                    if rec.correct:
                        correct += 1
                    total += 1
                return JsonResponse({'correct': correct, 'total': total})
            except:
                return super().http_method_not_allowed(request, *args, **kwargs)
        else:
            return super().http_method_not_allowed(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = list()
        for q in Question.objects.order_by('?')[:3]:
            opts = list()
            for ans in q.Answers.order_by('?'):
                opts.append({'oid': ans.pk,
                             'otxt': ans.dp_txt, })
            questions.append({'qid': q.pk,
                              'qtxt': q.dp_txt,
                              'qdesc': q.des,
                              'qaudio': q.audio.url if q.audio else '',
                              'options': opts, })
        context['quiz'] = questions
        return context
