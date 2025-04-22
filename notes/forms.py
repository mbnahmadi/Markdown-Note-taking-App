from django import forms
from notes.models import Notes


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'markdown_file']


        