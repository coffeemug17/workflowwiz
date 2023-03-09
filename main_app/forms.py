from django import forms
from django.forms import ModelForm
from .models import Comment, Task

class DateInput(forms.DateInput):
    input_type = 'date'

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']
    widgets = {
            'comment': forms.Textarea(attrs={'style':'width: 100%; height: 50px; border: solid 1px #ee6c4d'})
        }


class TaskForm(ModelForm):

    class Meta:
       model = Task
       fields = ['title', 'assignee', 'description', 'due_date', 'priority']
       widgets = {
            'due_date': DateInput(),
        }


