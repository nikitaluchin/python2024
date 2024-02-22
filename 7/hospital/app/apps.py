from django.apps import AppConfig
# from django.db import connection


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        # не делай так, ето плохо
        # cursor = connection.cursor()
        # cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='app_person';")
        # res = cursor.fetchall()
        # print(res)
        pass