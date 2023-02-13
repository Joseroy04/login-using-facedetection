# forms.py
from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    photo = forms.ImageField()

class LoginForm(forms.Form):
    student_id = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    # webcam_photo = forms.ImageField(required=False)
