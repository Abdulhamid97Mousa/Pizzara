from django.db import models
import uuid
from project.models import Project
from account.models import User


class TodoList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name='todolists', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.name