import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Member(AbstractUser):
    birth = models.DateField(null=True, blank=True, default=datetime.date.fromtimestamp(0000000000000))
    is_athlete = models.BooleanField(default=True, null=True, blank=True)
    is_coach = models.BooleanField(default=False, null=True, blank=True)
    coach_selected = models.BooleanField(default=False, null=True, blank=True)