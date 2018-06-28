from django import forms

from .models import Soccer

class SoccerForm(forms.ModelForm):

    class Meta:
        model = Soccer
        fields = ('title', 'text',)