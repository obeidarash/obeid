from django.urls import path
from .views import ProjectList, project_detail

app_name = 'projects'
urlpatterns = [
    path('projects', ProjectList.as_view(), name="list"),
    path('projects/<int:id>/<slug:slug>', project_detail, name="detail"),
]
