from django.shortcuts import render


def contact(request):
    context = {
        'title': 'contact'
    }
    return render(request, 'contact/contact.html', context)
