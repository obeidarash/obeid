from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, Category, Tag


class ProjectTag(ListView):
    # todo: this class must be improve (does not show the good result)
    template_name = 'project/projects.html'
    context_object_name = 'projects'
    paginate_by = 10
    ordering = ['-update']

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        print(tag_slug)
        tag = Tag.objects.filter(slug=tag_slug).first()
        print(tag)
        if tag is None:
            raise Http404("Tag Does Not Exist")
        else:
            return Project.objects.projects_by_tag(tag)


class ProjectCategory(ListView):
    # todo: this class must be improve (does not show the good result)
    template_name = 'project/projects.html'
    context_object_name = 'projects'
    paginate_by = 10
    ordering = ['-update']

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = Category.objects.filter(slug=category_slug).first()
        if category is None:
            raise Http404("Category Does Not Exist")
        else:
            return Project.objects.projects_by_category(category)


class ProjectList(ListView):
    model = Project
    queryset = Project.objects.all_published_projects()
    context_object_name = 'projects'
    paginate_by = 10
    ordering = ['-update']
    template_name = 'project/projects.html'


def project_detail(request, project_id):
    # todo: show slug of the project in the url
    project = Project.objects.published_project(project_id)
    if project is None:
        raise Http404('Ops!')
    tag: Tag = Tag.objects.first()
    tags = project.tag.all()
    category: Category = Category.objects.first()
    categories = project.category.all()
    # print(tag.project_set.all())
    context = {
        'project': project,
        'tags': tags,
        'categories': categories
    }
    return render(request, 'project/project.html', context)
