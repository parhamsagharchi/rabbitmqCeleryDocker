from celery_main.celery import app

import sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '../data')))
from src.scrapper import scrapper


@app.task(bind=True, default_retry_delay=10)
def do_work(self, handle):
    print('handle received ' + handle)
    scrapper(handle)
