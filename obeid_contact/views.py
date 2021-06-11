from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm, ScrapeForm
from .models import Contact, Scrape
import requests
from bs4 import BeautifulSoup
import goslate
from background_task import background
import datetime


@background(schedule=10)
def update():
    s = Scrape.objects.first().delete()


@login_required(login_url='/admin')
def scrape(request):
    scrape_form = ScrapeForm(request.POST or None)
    if scrape_form.is_valid():
        url = scrape_form.cleaned_data.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', attrs={'class': 'jojo', 'id': 'title-large-bold'}).text
        # gs = goslate.Goslate()
        # title = gs.translate(title, 'fa')
        rows = soup.find_all('div', attrs={'class': 'div-table-col-right'})
        color = rows[5].text
        size = rows[4].text
        Scrape.objects.create(user=request.user, url=url, title=title, color=color, size=size)
        scrape_form = ScrapeForm()
        update()
        redirect('scrape')

    context = {
        'title': 'Scraper - Test',
        'scrape_form': scrape_form
    }
    return render(request, 'scrape.html', context)


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
        'contact': contact_form,
        'time': datetime.datetime.now()
    }
    return render(request, 'contact/contact.html', context)
