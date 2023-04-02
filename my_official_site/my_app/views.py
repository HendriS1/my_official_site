from django.shortcuts import render
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def index(request):
    """
    This method will take a http request and returns a http
    response. For example HTML documents

    :param request: http request

    :return: http response home.html. Goes to the home page.
    """
    return render(request, 'my_app/home.html')


def events(request):
    """
    This method will take a http request and return a http 
    response. For example HTML documents
    Displays all the objects in models.py

    :param request: http request

    :return: http response event.html. Goes to events page
    """
    all_events = Event.objects.all()
    return render(request, 'my_app/event.html',
                  {'all_events': all_events})


def user_login(request):
    """
    This method will take a http request and returns a http
    response. For example HTML documents

    :param request: http request

    :return: http response login.html. Goes to the login page.
    """
    return render(request, 'my_app/login.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('login')
        )
    else:
        login(request, user)
    return HttpResponseRedirect(
        reverse('show_user')
    )


def show_user(request):
    print(request.user.username)
    return render(request, 'my_app/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(
                reverse('login')
            )
    else:
        form = UserCreationForm()
    return render(request, 'my_app/create_user.html', {
        'form': form,
    })


def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out!!")
    return HttpResponseRedirect('/')
