from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Project, Customer, Category, Tag


class ProjectList(ListView):
    model = Project
    queryset = Project.objects.all_published_projects()
    context_object_name = 'projects'
    paginate_by = 1
    ordering = ['-id']
    template_name = 'project/projects.html'


def project_detail(request, project_id):
    project = Project.objects.published_project(project_id)
    if project is None:
        raise Http404('Ops!')
    # customer = Customer.objects.filter(id=project.customer.id)
    print(project.customer)
    print(project.category)
    context = {
        'project': project,
    }
    return render(request, 'project/project.html', context)
