from django.urls import path

from .views import index, engagement

urlpatterns = [
    path('', index, name='index'),
    path('engagement', engagement, name='engagement'),
]
