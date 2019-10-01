from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home, name='student_home'),
    path('results/zip_code=<str:my_zip_code>', views.results, name = 'results-afterSearch'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)