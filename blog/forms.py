from django import forms

from .models import Soccer, Comment

class SoccerForm(forms.ModelForm):

    class Meta:
        model = Soccer
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)