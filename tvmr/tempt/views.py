from datetime  import datetime
from django.shortcuts import render
from .models import Student

def response_view(request):
    students = Student.objects.all().filter(roll__gte=5).values() # QuerySet of dicts

    date = datetime.now()
    name = ['mizan','sizan','akb']

    
    context = {
        'date' : date,
        'name' : name
     }
    return render(request, 'tempt/index.html', context)
