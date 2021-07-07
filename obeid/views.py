from django.shortcuts import render
from obeid_projects.models import Project


def home(request):
    latest_projects: Project = Project.objects.filter(publish=True, progress__range=[0, 99]).order_by('-create')[:5]
    completed_projects: Project = Project.objects.filter(progress=100, publish=True).order_by('-update')[:5]
    context = {
        'title': 'Home',
        'latest_projects': latest_projects,
        'completed_projects': completed_projects
    }
    return render(request, 'home.html', context)
