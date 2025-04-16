from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField()
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default=)
