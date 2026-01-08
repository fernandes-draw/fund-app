from django.db import models
import uuid


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default="PROJETO")
    priority = models.CharField(
        max_length=30, choices=PRIORITY_CHOICES, default="BAIXA")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
