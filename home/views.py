from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "home/index.html")


def engagement(request: HttpRequest) -> HttpResponse:
    return render(request, "home/engagement.html")