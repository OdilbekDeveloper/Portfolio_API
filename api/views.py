from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
import requests
# Create your views here.


def Main(request):
    return True


def SendContact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        message = request.POST['message']
        a = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            message=message
        )


        id = 6049386128
        token = '6085140316:AAE57gJ5v-SsucVkJ9X21Zl8qOf6QOLBvDs'
        text = 'Yangi xabar!\n' + 'F.I.SH: ' + first_name + ' ' + last_name + '\nTelefon raqam: ' + phone + '\nXabar: ' + message
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(id.tg_id) + '&text=' + text)

        ser = ContactLoader(a)
        return Response(ser.data, status=status.HTTP_200_OK)

