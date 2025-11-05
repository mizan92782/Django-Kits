from django.contrib.auth import login, authenticate
from core.models import User
from django.shortcuts import HttpResponse

def auto_login(request):
    username = 'fuser2'
    password = '1232'

    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  # logs in the user for this session
        return HttpResponse(f"Logged in user: {user.username}")
    else:
        return HttpResponse("Invalid credentials")

