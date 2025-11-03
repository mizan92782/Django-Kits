from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        # model এর কোন fields show করতে চাও, সেটা এখানে
        fields = ['first_name', 'last_name','email','number' ,'age', 'bio', 'position', 'cv']

        # Optional: field এর labels customize করা
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'bio': 'Bio',
            'email' : 'E-mail',
            'number' : 'Number',
            'position': 'Position',
            'cv': 'Upload CV',
        }

        # Optional: widgets use করে form সুন্দর করা
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
        }
