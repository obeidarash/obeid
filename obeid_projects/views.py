from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Project, Customer, Category


class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'
    paginate_by = 5
    template_name = 'project/projects.html'


def project_detail(request, project_id):
    project = Project.objects.published_project(project_id)
    context = {
        'project': project,
    }
    return render(request, 'project/project.html', context)
