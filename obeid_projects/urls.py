from django.urls import path
from .views import ProjectList, project_detail, ProjectCategory, ProjectTag

app_name = 'project'
urlpatterns = [
    path('projects', ProjectList.as_view(), name="list"),
    path('projects/<slug:project_slug>', project_detail, name="detail"),
    path('projects/cat/<slug:category_slug>', ProjectCategory.as_view(), name="category"),
    path('projects/tag/<slug:tag_slug>', ProjectTag.as_view(), name="tag"),
]
