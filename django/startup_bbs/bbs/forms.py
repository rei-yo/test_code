from django import forms 
from .models import Topic, Album, Document

class TopicForm(forms.ModelForm):

    class Meta:
        model   = Topic
        fields  = [ "comment" , 'category', 'photo']


class AlbumForm(forms.ModelForm):

    class Meta:
        model   = Album
        fields  = ['photo']

class DocumentForm(forms.ModelForm):

    class Meta:
        model   = Document
        fields  = ['file']