# forms.py
from django import forms

class UploadCrimeDataForm(forms.Form):
    file = forms.FileField()