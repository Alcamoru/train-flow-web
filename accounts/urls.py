from django.urls import path, include

from .views import signup, login_user, logout_user
urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login_user, name='login'),
]
