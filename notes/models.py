from django.db import models

class Note(models):
    text = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

