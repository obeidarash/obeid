from django.urls import path
from .views import youtube

app_name = 'tools'
urlpatterns = [
    path('youtube', youtube, name="youtube"),

]
