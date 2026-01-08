from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ("ACABAMENTO", "ACABAMENTO"),
    ("AGUARDANDO", "AGUARDANDO"),
    ("ALTERAÇÃO", "ALTERAÇÃO"),
    ("APROVADO", "APROVADO"),
    ("CANCELADO", "CANCELADO"),
    ("CONCLUÍDO", "CONCLUÍDO"),
    ("CONF PASTA USINAGEM", "CONF PASTA USINAGEM"),
    ("DISPOSITIVO", "DISPOSITIVO"),
    ("LIBERADO", "LIBERADO"),
    ("MONTAR PASTA USINAGEM", "MONTAR PASTA USINAGEM"),
    ("NÃO INICIADO", "NÃO INICIADO"),
    ("ORÇAMENTO", "ORÇAMENTO"),
    ("PARADO", "PARADO"),
    ("PRODUÇÃO", "PRODUÇÃO"),
    ("PROJETO", "PROJETO"),
    ("REVISÃO", "REVISÃO"),
    ("USINAGEM", "USINAGEM"),
]

PRIORITY_CHOICES = [
    ("BAIXA", "BAIXA"),
    ("MÉDIA", "MÉDIA"),
    ("ALTA", "ALTA"),
]


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default="PROJETO")
    priority = models.CharField(
        max_length=30, choices=PRIORITY_CHOICES, default="BAIXA")
    start_date = models.DateField()
    due_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["-created_at",]

    def days_until_due(self):
        if self.due_date:
            # get current date
            current_date = timezone.now().date()
            return (self.due_date - current_date).days
        return None

    def priority_color(self):
        if self.priority == "BAIXA":
            color = "success"
        elif self.priority == "MÉDIA":
            color = "warning"
        else:
            color = "danger"
        return color
