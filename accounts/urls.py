from django.urls import path, include

from .views import signup, login_user, logout_user, info, switch_profile
urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login_user, name='login'),
    path('info', info, name='info'),
    path('logout', logout_user, name='logout'),
    path('switch-profile', switch_profile, name='switch-profile'),
]
