from django.apps import AppConfig


class OtpvalidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'otpvalid'

    def ready(self):
         import otpvalid.signals