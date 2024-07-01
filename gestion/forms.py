from django import forms
from .models import Patients

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['first_name', 'last_name', 'phone', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}), 
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
             
        }