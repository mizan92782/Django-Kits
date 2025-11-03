# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . form import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('its created')
    else:
        form = StudentForm()
    return render(request, 'forms.html', {'form': form})

def success(request):
    return render(request, 'success.html')
