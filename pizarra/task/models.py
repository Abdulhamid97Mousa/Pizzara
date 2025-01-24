from django.db import models
import uuid
from todolist.models import TodoList
from account.models import User
from project.models import Project

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    todolist = models.ForeignKey(TodoList, related_name='tasks', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
