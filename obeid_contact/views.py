from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contact(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        subject = contact_form.cleaned_data.get('subject')
        email = contact_form.cleaned_data.get('email')
        content = contact_form.cleaned_data.get('content')
        Contact.objects.create(name=name, subject=subject, email=email, content=content)
        contact_form = ContactForm()
        # todo: redirect and show message
    context = {
        'title': 'Contact Me',
        'contact': contact_form
    }
    return render(request, 'contact/contact.html', context)
