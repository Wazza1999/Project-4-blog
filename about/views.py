from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForms

"""Walkthrough code for About collaboration View"""


def about_me(request):

    if request.method == "POST":
        collaborate_form = CollaborateForms(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request recieved! I endeavour to respond within 2 working days")  # noqa
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForms()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )
