from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('user', 'comment',)

    widgets = {
      'user':forms.TextInput(attrs={'class':'form-control'}),
      'comment':forms.Textarea(attrs={'class':'form-control'}),
    }