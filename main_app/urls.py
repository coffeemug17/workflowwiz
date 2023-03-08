from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('projects/<int:project_id>/', views.projects_detail, name='detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('projects/<int:project_id>/add_comment/', views.add_comment, name='add_comment'),
    path('projects/<int:project_id>/<int:task_id>/', views.tasks_detail, name='tasks_detail'),
    path('projects/<int:project_id>/tasks_create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('projects/<int:project_id>/<int:pk>/tasks_update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('projects/<int:project_id>/<int:pk>/tasks_delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('projects/<int:project_id>/assoc_member/<int:member_id>', views.assoc_member, name='assoc_member'),
    path('projects/<int:project_id>/unassoc_member/<int:member_id>', views.unassoc_member, name='unassoc_member'),
]