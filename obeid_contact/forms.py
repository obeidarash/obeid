from django import forms
from django.core import validators


class ScrapeForm(forms.Form):
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Link',
        validators=[
            validators.URLValidator(message='{url} not a url'),
        ]
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Name / Company name',
        validators=[
            validators.MaxLengthValidator(limit_value=128, message='Your name is too long'),
            validators.MinLengthValidator(limit_value=5, message='Your name is too short'),
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Subject',
        validators=[
            validators.MaxLengthValidator(limit_value=256, message='Subject is too long'),
            validators.MinLengthValidator(limit_value=8, message='Subject is too short'),
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Email',
        validators=[
            validators.EmailValidator(message="Your email address isn't correct"),
        ]
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': '', 'class': 'form-control', 'rows': 7}),
        label='Content',
        validators=[
            validators.MaxLengthValidator(limit_value=2048, message='Your message is too long'),
            validators.MinLengthValidator(limit_value=16, message='Your message is too short'),
        ]
    )
