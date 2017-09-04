# main/tasks.py

import logging
from datetime import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from bproject.celery import app


@app.task
def send_verification_email(user_id):

    try:
        user = User.objects.get(pk=user_id)
        user.profile.phone_number = 380951102135
        user.profile.save()
        # send_mail(
        #     'Verify your QuickPublisher account',
        #     'Follow this link to verify your account: '
        #     'http://localhost:8000%s' % reverse('verify', kwargs={
        #         'uuid': str(user.verification_uuid)}),
        #     'from@quickpublisher.dev',
        #     [user.email],
        #     fail_silently=False,
        # )
    except User.DoesNotExist:
        logging.warning(
            "Tried to send verification email to non-existing user '%s'" % user_id)


@app.task
def every_minute():

    try:
        user = User.objects.get(pk=14)
        user.profile.phone_number = datetime.now()
        user.profile.save()
        # send_mail(
        #     'Verify your QuickPublisher account',
        #     'Follow this link to verify your account: '
        #     'http://localhost:8000%s' % reverse('verify', kwargs={
        #         'uuid': str(user.verification_uuid)}),
        #     'from@quickpublisher.dev',
        #     [user.email],
        #     fail_silently=False,
        # )
    except User.DoesNotExist:
        logging.warning(
            "Tried to send verification email to non-existing user '%s'" % user_id)