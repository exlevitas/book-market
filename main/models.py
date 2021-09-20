from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    price = models.FloatField(null=True, blank = True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    def __str__(self):
        return self.title

class Absuser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать сообщения?')
    class Meta(AbstractUser.Meta):
        pass
