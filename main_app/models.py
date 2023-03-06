from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    completion = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.name} {self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})
    
    

    