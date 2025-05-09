from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget
from django import forms
"""My code for adding, deleting and updating posts"""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "content", "featured_image", "status"]
        widgets = {
            'content': SummernoteWidget(),
        }


"""Walkthrough code for Comments"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
