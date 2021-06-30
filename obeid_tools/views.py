from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import YoutubeForm
from pytube import YouTube


def youtube(request):
    yt = ""
    youtube_form = YoutubeForm(request.POST or None)
    if request.method == "POST" and youtube_form.is_valid():
        url = youtube_form.cleaned_data.get('url')
        yt = YouTube(url)
        print(yt.streams.first())
        youtube_form = YoutubeForm()
    context = {
        'youtube': youtube_form,
        'yt': yt
    }
    return render(request, 'tools/youtube.html', context)
