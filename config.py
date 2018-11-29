import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'm6dNHgWsA!A6T%@TB#PhXUC46wuU9NRxQ$H'
