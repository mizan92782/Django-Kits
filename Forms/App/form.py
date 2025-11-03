# myapp/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
        labels = {
            'name': 'নাম',
            'email': 'ইমেইল',
            'age': 'বয়স',
            'password': 'পাসওয়ার্ড'
        }
        help_texts = {
            'age': 'বয়স অবশ্যই 18 এর বেশি হতে হবে',
        }
        error_messages = {
            'name': {
                'required': 'নাম অবশ্যই দিতে হবে',
                'max_length': 'নাম 50 অক্ষরের বেশি হবে না'
            },
            'email': {
                'required': 'ইমেইল দিন',
                'invalid': 'সঠিক ইমেইল দিন',
                'unique': 'এই ইমেইল আগে থেকেই আছে'
            },
            'age': {
                'required': 'বয়স দিতে হবে'
            },
            'password': {
                'required': 'পাসওয়ার্ড দিন'
            }
        }

    # Field-level validation
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('বয়স কমপক্ষে 18 হতে হবে')
        return age

    # Form-level validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("পাসওয়ার্ড মিলছে না")
