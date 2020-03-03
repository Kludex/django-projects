from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from twilio.rest import Client


def sms(request):
    msg = ('Hi there!')
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                  from_=settings.TWILIO_NUMBER,
                                  body=msg)
    return HttpResponse('msg sent!', 200)