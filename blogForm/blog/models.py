from django.db import models

class BlogPost(models.Model):
    username = models.CharField(max_length = 130)
    text = models.TextField()