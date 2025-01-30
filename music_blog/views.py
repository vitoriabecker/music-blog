from django.shortcuts import render, get_object_or_404
from .models import Song

"""
views ideas:
song_list - going to be home page
song_detail - shows the lyrics or maybe a curiosity about the song

song_mp3 - kkkkkk, preciso de uma view pra transformar em mp3, correto?
sessao de comentario? talvez, nao sei

vai ter create? nao sei se faz sentido aqui, acho q o melhor eh deixar simples mesmo

"""

def song_list(request):
  template_name = 'song_list.html'
  songs = Song.objects.all()
  return render(request, 'music_blog/song_list.html', {'songs':songs})

def song_detail(request, pk):
  template_name = 'song_detail.html'
  song = get_object_or_404(Song, pk=pk)
  return render(request, 'music_blog/song_detail.html', {'song':song})