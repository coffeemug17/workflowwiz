from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Task, User
from .forms import CommentForm, TaskForm, ProjectForm

# Create your views here.
class ProjectCreate(LoginRequiredMixin, CreateView):
  model = Project
  form_class = ProjectForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = ['title', 'description']


class ProjectDelete(LoginRequiredMixin, DeleteView):
  model = Project
  success_url = '/projects'

@login_required
def add_comment(request, project_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.project_id = project_id
    new_comment.user = request.user
    new_comment.save()
  return redirect('detail', project_id=project_id)


class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  form_class = TaskForm

  def form_valid(self, form):
    form.instance.project_id = self.kwargs['project_id']
    return super().form_valid(form)
    


class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['title', 'assignee', 'description', 'due_date', 'priority', 'completion']

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  # success_url = '/projects'
  def get_success_url(self):
      return reverse(
          'detail',
          kwargs={
              'project_id': self.object.project.id,
          }
      )

def home(request):
    return render(request, 'home.html')

@login_required
def projects_index(request):
  projects = Project.objects.filter(user=request.user)
  assoc_projects = Project.objects.filter(members=request.user)
  return render(request, 'projects/index.html', {
    'projects': projects,
    'assoc_projects' : assoc_projects
  })

@login_required
def projects_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  tasks = project.task_set.all()
  id_list = project.members.all().values_list('id')
  members_not_assoc = User.objects.exclude(id__in=id_list).exclude(id=project.user.id)
  comment_form = CommentForm()
  return render(request, 'projects/detail.html', {
    'project': project,
    'tasks' : tasks,
    'members': members_not_assoc,
    'comment_form' : comment_form
  })

@login_required
def tasks_detail(request, project_id, task_id):
  project = Project.objects.get(id=project_id)
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', {
    'project': project,
    'task' : task
  })

def assoc_member(request, project_id, member_id):
  Project.objects.get(id=project_id).members.add(member_id)
  return redirect('detail', project_id=project_id)

def unassoc_member(request, project_id, member_id):
  Project.objects.get(id=project_id).members.remove(member_id)
  return redirect('detail', project_id=project_id)

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

