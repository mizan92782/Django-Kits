from django.apps import AppConfig


class ApplicantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Applicants'


    def ready(self):
            import Applicants.signals  # <--- এখানে import
