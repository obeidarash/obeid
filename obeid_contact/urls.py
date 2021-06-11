from django.urls import path
from .views import contact, scrape

urlpatterns = [
    path('contact', contact, name="contact"),
    path('scrape', scrape, name="scrape"),

]
