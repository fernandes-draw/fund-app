from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from projects.models import Project


STATUS_CHOICES = [
    ("To Do", "To Do"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed"),
]

PRIORITY_CHOICES = [
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High"),
]


class Task(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField()
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default="To Do")
    priority = models.CharField(
        max_length=30, choices=PRIORITY_CHOICES, default="Medium")
    start_date = models.DateField()
    due_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def days_until_due(self):
        if self.due_date:
            # get current date
            current_date = timezone.now().date()
            return (self.due_date - current_date).days
        return None

    def priority_color(self):
        if self.priority == "Low":
            color = "success"
        elif self.priority == "Medium":
            color = "warning"
        else:
            color = "danger"
        return color
