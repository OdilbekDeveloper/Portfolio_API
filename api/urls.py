from django.urls import path
from .views import *
urlpatterns = [
    path('contact/', SendContact),
    path('newsletter/', Add_Newsletter)
]