from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

PRIORITIES = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    completion = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'({self.title} {self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    # later turn into drop down off assigned users
    assignee = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    due_date = models.DateField('Due Date')
    completion = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITIES,
        default=PRIORITIES[0][0]
    )

    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title



