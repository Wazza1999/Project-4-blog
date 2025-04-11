from .models import Comment
from django import forms

"""Walkthrough code for Comments"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
