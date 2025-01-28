from django.shortcuts import render
from .models import Song

"""
views ideas:
song_list - going to be home page
song_detail - shows the lyrics or maybe a curiosity about the song

song_mp3 - kkkkkk, preciso de uma view pra transformar em mp3, correto?
sessao de comentario? talvez, nao sei


"""


def song_list(request):
  template_name = 'song_list.html'
  songs = Song.objects.all()
  return render(request, template_name, {'songs':songs})