from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('', include('obeid_projects.urls', namespace='project')),
    path('', include('obeid_tools.urls', namespace='tools')),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header = "Obied Arash"
admin.site.site_title = "Obeid Arash"
admin.site.index_title = "Welcome to Obied Arash Admin Area"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
