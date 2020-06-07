from django.db import models

class BlogPost(models.Model):
    username = models.CharField(max_length=127)
    text = models.TextField()