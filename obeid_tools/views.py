from django.shortcuts import render


def youtube(request):
    context = {}
    return render(request, 'tools/youtube.html', context)
