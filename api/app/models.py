from django.db import models

class Message(models.Model):
    id = models.IntegerField()
    ts = models.IntegerField()
    txt = models.TextField()
    sender = models.TextField()

    class Meta:
        ordering = ('id',)
