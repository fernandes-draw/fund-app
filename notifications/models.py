from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class NotificationManager(models.Manager):
    def for_user(self, user):
        return self.filter(recipient=user)

    def unread(self, user):
        return self.for_user(user).filter(read=False)

    def read(self, user):
        return self.for_user(user).filter(read=True)


class Notification(models.Model):
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications", verbose_name="Destinatário")
    actor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="actions", verbose_name="Ator")
    verb = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=255)
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField()
    read = models.BooleanField(default=False)

    objects = NotificationManager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"

    def __str__(self):
        return f"{self.actor} {self.verb} {self.content_object}"

    @property
    def notification_timer_formatted(self):
        return self.created_at.strftime("%d %b %I %M %p")
