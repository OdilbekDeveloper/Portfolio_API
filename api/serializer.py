from rest_framework import serializers
from .models import *

class ContactLoader(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterLoader(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'