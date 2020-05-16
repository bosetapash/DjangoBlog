from django.apps import AppConfig
import logging

class UsersConfig(AppConfig):
    name = 'users'

def ready(self):
        logging.INFO("IMporting Signals............")
        import users.signals
