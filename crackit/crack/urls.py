from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from .views import *

app_name = 'crack'
urlpatterns = [

    path('', contactUs, name='contact'),
    path('register/', RegisterTemplateView.as_view(), name='register'),

]