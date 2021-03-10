import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

RABBITMQ_DEFAULT_USER = os.environ.get("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.environ.get("RABBITMQ_DEFAULT_PASS")
TARGET_FILE = os.environ.get("TARGET_FILE")
LOCAL_IP = os.environ.get("LOCAL_IP")
