#_______________________________

from django.apps import AppConfig

class VideogameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videogame'

    # def ready(self):
    #     import videogame.signals  # Import any signals you may have for the app

