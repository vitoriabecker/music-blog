from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, Comment
from .forms import CommentForm
import requests 
"""
song_mp3 - kkkkkk, preciso de uma view pra transformar em mp3, correto?

"""


def song_list(request):
  template_name = 'song_list.html'
  songs = Song.objects.all()
  return render(request, template_name, {'songs':songs})


def song_detail(request, pk):
  template_name = 'song_detail.html'
  song = get_object_or_404(Song, pk=pk)
  comments = song.comments.all()

  params = {'track_name':song.title, 'artist_name':song.artist,}
  response = requests.get('https://lrclib.net/api/get', params=params)
  response = response.json()
  lyrics = response.get('plainLyrics')

  comment_form = CommentForm()

  return render(request, template_name, {'song':song,
                                          'comments':comments,
                                          'comment_form':comment_form,
                                          'lyrics': lyrics,})


def add_comment_to_song(request, pk):
  song = get_object_or_404(Song, pk=pk)
  comment_form = CommentForm(data=request.POST)

  if comment_form.is_valid():
    new_comment = comment_form.save(commit=False)
    new_comment.song = song
    new_comment.save()
    return redirect('song_detail', pk=pk)
  else:
    return redirect('song_list')

 