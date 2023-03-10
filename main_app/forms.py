from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from .models import Comment, Task, Project

class DateInput(forms.DateInput):
    input_type = 'date'

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']
    widgets = {
            'comment': forms.Textarea(attrs={
                'style':'width: 95%; height: 50px; border-radius: 10px; border: solid 1px #ee6c4d;'})
        }


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'assignee', 'description', 'due_date', 'priority']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'assignee': TextInput(attrs={'class': 'form-control', 'placeholder': 'Assignee'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description'}),
            'due_date': DateInput(attrs={'class': 'form-control'}),
        }

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Project title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
        }
