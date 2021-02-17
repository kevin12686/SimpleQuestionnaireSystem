from django.apps import AppConfig


class QuestionnaireConfig(AppConfig):
    name = 'questionnaire'

    def ready(self):
        from .signals import check_answer
