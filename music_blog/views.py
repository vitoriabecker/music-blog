from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, Comment
from .forms import CommentForm

"""
views ideas:
song_list - going to be home page
song_detail - shows the lyrics or maybe a curiosity about the song

song_mp3 - kkkkkk, preciso de uma view pra transformar em mp3, correto?
sessao de comentario? - talvez, nao sei

vai ter create? nao sei se faz sentido aqui, acho q o melhor eh deixar simples mesmo

"""

def song_list(request):
  template_name = 'song_list.html'
  songs = Song.objects.all()
  return render(request, 'music_blog/song_list.html', {'songs':songs})


def song_detail(request, pk):
  template_name = 'song_detail.html'
  song = get_object_or_404(Song, pk=pk)
  comments = song.comments.all()

  comment_form = CommentForm()

  return render(request, 'music_blog/song_detail.html', {'song':song,
                                                        'comments':comments,
                                                        'comment_form':comment_form,})


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

 