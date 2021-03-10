FROM python:3.9.2
ADD requirements.txt /app/requirements.txt
ADD ./celery_main/ /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT celery -A celery_main worker --concurrency=5 --loglevel=INFO