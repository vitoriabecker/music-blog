from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.song_list, name='song_list'),
  path('song/<int:pk>', views.song_detail, name='song_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)