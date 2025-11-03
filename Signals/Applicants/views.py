from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import ApplicantForm

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicantForm

def apply_page(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            return HttpResponse("User created successfully") 
        else:
            # এখানে form.errors দেখানো হচ্ছে
            errors = form.errors.as_json()  # JSON format
            # অথবা as_text() for plain text: errors = form.errors.as_text()
            return HttpResponse(f"User creation not successful. Errors: {errors}") 
    else:
        form = ApplicantForm()

    return render(request, 'application.html', {'form': form})
