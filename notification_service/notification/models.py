from django.db import models

# Create your models here.
class Notification(models.Model):
    username_ator = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    read = models.BooleanField(default=False)
    verb = models.CharField(max_length=20, default="postagem")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message