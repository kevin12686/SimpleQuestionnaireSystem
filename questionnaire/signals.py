from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Record


@receiver(m2m_changed, sender=Record.answers.through)
def check_answer(instance, action, *args, **kwargs):
    if action == 'post_add':
        if set(instance.question.Answers.filter(correct=True)) == set(instance.answers.all()):
            instance.correct = True
            instance.save()
