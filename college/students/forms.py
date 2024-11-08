from django import forms
from students.models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control p-2 g-col-6', 
                'placeholder': 'Enter Full Name'
            }),
            'pin_no': forms.TextInput(attrs={
                'class': 'form-control p-2 g-col-6', 
                'placeholder': 'Enter PIN No'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control p-2 g-col-6', 
                'placeholder': 'Enter Phone Number'
            }),
            'gmail': forms.EmailInput(attrs={
                'class': 'form-control p-2 g-col-6', 
                'placeholder': 'Enter Email'
            }),
            'branch': forms.TextInput(attrs={
                'class': 'form-control p-2 g-col-6', 
                'placeholder': 'Enter Branch'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control p-2 g-col-6', 
                'placeholder': 'Enter Age'
            }),
            'profile': forms.ClearableFileInput(attrs={
                'class': 'form-control p-2 g-col-6'
            }),
        }
