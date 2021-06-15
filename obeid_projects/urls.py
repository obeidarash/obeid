from django.urls import path
from .views import ProjectList, project_detail

app_name = 'project'
urlpatterns = [
    path('projects', ProjectList.as_view(), name="list"),
    path('projects/<int:project_id>', project_detail, name="detail"),
]
