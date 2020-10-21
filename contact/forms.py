from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['full_name', 'contact_subject', 'email', 'contact_body']

    full_name = forms.CharField(
        required=True,
        label='Full Name:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full Name'
        })
    )

    contact_subject = forms.CharField(
        required=True,
        label='Subject:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject'
        })
    )

    email = forms.EmailField(
        required=True,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    contact_body = forms.CharField(
        required=True,
        label='Please enter your message:',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message'
        })
    )
