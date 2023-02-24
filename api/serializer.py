from rest_framework import serializers
from .models import *

class ContactLoader(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'