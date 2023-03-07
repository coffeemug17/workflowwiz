from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Task

# Create your views here.
class ProjectCreate(LoginRequiredMixin, CreateView):
  model = Project
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = '__all__'


class ProjectDelete(LoginRequiredMixin, DeleteView):
  model = Project
  success_url = '/projects'


class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['title', 'assignee', 'description', 'due_date', 'priority']

  def form_valid(self, form):
    form.instance.project_id = self.kwargs['project_id']
    return super().form_valid(form)
    


class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['title', 'assignee', 'description', 'due_date', 'priority']

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  success_url = '/projects/<int:project_id>/'

def home(request):
    return render(request, 'home.html')

@login_required
def projects_index(request):
  projects = Project.objects.filter(user=request.user)
  return render(request, 'projects/index.html', {
    'projects': projects
  })

@login_required
def projects_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  tasks = project.task_set.all()
  return render(request, 'projects/detail.html', {
    'project': project,
    'tasks' : tasks
  })



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

