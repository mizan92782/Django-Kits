from typing import Required
import django.core.exceptions
from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout



# ! Count user
def UserCount(request):
  user =User.objects.all()

  for x in user:
    print(x.username  ,   x.email)
  return HttpResponse("counting user ")


#! create a new User
def UserCreate(request):
  name ="araidf"
  email= 'aarasif@gamil.com'
  password= '45466'


  #* existing use check
  if User.objects.filter(Q(username=name) & Q(email=email)).exists():
    messages.error(request, 'Username already exists!')
    return HttpResponse(f'User cannot created: {message } - {password} - {email}')


  user = User.objects.create_user(
    username=name,
    password=password,
    email=email
  )


  return  redirect('user_count')



#! Home page
from django.contrib.auth.decorators import login_required

@login_required
def HomePage(request):
  return render(request,'auth/home.html')

# ! Login

def LoginPage(request):
  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid credentials!')
  return render(request, 'auth/login.html')
