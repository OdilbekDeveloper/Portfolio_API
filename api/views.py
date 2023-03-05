from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
import requests
# Create your views here.


def Main(request):
    return True


@api_view(['POST'])
def SendContact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        print(last_name)
        phone = request.POST.get('phone')
        print(phone)
        message = request.POST.get('message')
        print(message)
        a = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            message=message
        )


        id = 6276309627
        token = '6033803581:AAH4oYcXR6XMi3UfTUPW5rL6DYXx8xoVJW0'
        text = 'Yangi xabar!\n' + 'F.I.SH: ' + first_name + ' ' + last_name + '\nTelefon raqam: ' + phone + '\nXabar: ' + message
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(id) + '&text=' + text)

        return Response(status=200)

@api_view(['POST'])
def Add_Newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        a = Newsletter.objects.create(email=email)

        return Response(status=201)
