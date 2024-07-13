from django.urls import path, include

from .views import *
urlpatterns = [
    path('coach', coach, name='coach'),
    path('calendar', calendar, name='calendar'),
]
