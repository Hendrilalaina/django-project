from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
