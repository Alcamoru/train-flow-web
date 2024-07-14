from django.contrib.auth import get_user_model, login, authenticate, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect

from accounts.models import Member

# Create your views here.

MemberModel: Member = get_user_model()


def info(request):
    member: Member = request.user
    if member:
        if not member.is_athlete and member.is_coach:
            return render(request, 'accounts/info.html', {'member': member})
        if member.is_athlete and not member.athlete_profile_completed:
            context = {"athlete_profile": "not completed"}
            return render(request, "accounts/info.html", context)
        return render(request, "accounts/info.html")
    else:
        return redirect("index")


def signup(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        if email and password:
            member = Member.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
            login(request, member)
            return redirect("profile-signup")

    return render(request, "accounts/signup.html")


def login_user(request: HttpRequest):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            member = authenticate(username=username, password=password)
            if member:
                login(request, member)
                return redirect("index")
        return render(request, "accounts/login.html")
    return redirect("index")


def logout_user(request: HttpRequest):
    logout(request)
    return redirect("index")


def switch_profile(request: HttpRequest):
    member: Member = request.user
    if member.coach_selected:
        member.coach_selected = False
        member.save()
    else:
        member.coach_selected = True
        member.save()
    return redirect("index")


def profile_signup(request: HttpRequest):
    return render(request, "accounts/profile_signup.html")


def athlete_signup(request: HttpRequest):
    return render(request, "accounts/athlete_signup.html")
