from celery.task.schedules import crontab
from celery.decorators import periodic_task,task
from celery.utils.log import get_task_logger
from django.conf import settings
from .models import *
import os
import sys
import subprocess
import pathlib
from django.utils import timezone

def save_cc_api_data(task):
	print("in save cc")


def check_rules_and_send_email(task):
	print("in check rules and email")