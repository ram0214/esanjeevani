

from django.urls import path
from mainapp.views import *

urlpatterns = [
    path("", home, name="home"),
    path("body_picker/", body_picker, name="body_picker"),
    path("organs/", organ, name="organ"),
    path("bot/", chatbot, name="chatbot"),
    path("doctor/", doctor_page, name="doctor"),
    path("general/", general_problem, name="general_problem"),
]
