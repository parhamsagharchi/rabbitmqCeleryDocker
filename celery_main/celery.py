import sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '../data')))

from src.setting import RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS, LOCAL_IP
from celery import Celery

app = Celery(
    'celery_main',
    broker=f'amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{LOCAL_IP}:5672/',
    backend='rpc://',
    include=['celery_main.task_receiver']
)
