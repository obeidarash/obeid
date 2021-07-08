from django.shortcuts import render, Http404
from .forms import YoutubeForm
import pafy
from django.contrib.auth.decorators import login_required
from .models import Youtube


# from pytube import YouTube
# import requests
# from django.http import HttpResponseRedirect


@login_required(login_url='home')
def youtube(request):
    videos = ''
    video = ''
    youtube_form = YoutubeForm(request.POST or None)
    if request.method == "POST" and youtube_form.is_valid():
        url = youtube_form.cleaned_data.get('url')
        try:
            video = pafy.new(url)
        except:
            raise Http404('This is not a youtube url!')
        if video:
            videos = video.videostreams
            youtube_form = YoutubeForm()
            Youtube.objects.create(url=url, title=video.title, id=video.videoid)

    context = {
        'youtube': youtube_form,
        'video': video,
        'videos': videos,
    }
    return render(request, 'tools/youtube.html', context)
