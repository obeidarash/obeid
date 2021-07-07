from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import YoutubeForm
from pytube import YouTube
import requests
import pafy
from django.contrib.auth.decorators import login_required


@login_required(login_url='home')
def youtube(request):
    video = ''
    youtube_form = YoutubeForm(request.POST or None)
    if request.method == "POST" and youtube_form.is_valid():
        url = youtube_form.cleaned_data.get('url')
        video = pafy.new(url)
        youtube_form = YoutubeForm()
    context = {
        'youtube': youtube_form,
        'video': video
    }
    return render(request, 'tools/youtube.html', context)
