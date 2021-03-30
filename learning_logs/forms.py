from django import forms
from .models import Topic, Entry


class TopicForm(form.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
