from time import time
from django.db import models
from workspace.models import Workspace


class Priority(models.Model):
    priority_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.priority_name

class Status(models.Model):
    status_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.status_name
    
class Task(models.Model): 
    name = models.CharField(max_length=100)
    workspace_id = models.ForeignKey(Workspace, related_name='task', on_delete=models.CASCADE)
    priority_id = models.ForeignKey(Priority, related_name='tasks', on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, default='1', related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self) -> str:
        return self.name
    