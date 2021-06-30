from django import forms
from django.core import validators


class YoutubeForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'https://www.youtube.com/watch?v=LLJhUVkgcvQ',
        'class': 'form-control',
        'value': 'https://www.youtube.com/watch?v=LLJhUVkgcvQ'
    }), required=False)

# , validators=[validators.URLValidator(), ]
