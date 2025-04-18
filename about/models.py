from django.db import models
from cloudinary.models import CloudinaryField

"""Walkthrough code for the about page"""


class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField(default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


""" Walkthrough code for the collaboration form"""


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
