from django.urls import path, include

from .views import index, engagement
urlpatterns = [
    path('', index, name='index'),
    path('engagement', engagement, name='engagement'),
]
