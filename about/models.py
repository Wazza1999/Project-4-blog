from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class About(models.Model):
    title = models.Charfield(max_length=200, unique=True)
    content = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="about_posts")


def __str__(self):
    return f"{self.title}| written by {self.author}"
