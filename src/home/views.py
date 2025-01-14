import json
from pathlib import Path

from decouple import config
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm


def load_data():
    # Path to the JSON file
    data_file = Path(__file__).resolve().parent.parent / "static/js/data.json"

    # Load JSON data
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        data = {}

    return data


def process_contact_form(request):
    form = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Send email
            send_mail(
                subject=f"Message from {name}",
                message=f"From: {email}\n\nMessage:\n{message}",
                from_email=email,
                recipient_list=[config("EMAIL_HOST_USER")],
                fail_silently=False,
            )
            success = True
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(
                request,
                "There was an error with your submission. Please check your input.",
            )

    return {"form": form, "success": success}


def home(request):
    # Load data
    data = load_data()

    # Process contact form
    contact_context = process_contact_form(request)

    # If the form was successfully submitted, redirect to avoid form resubmission
    if contact_context.get("success"):
        return HttpResponseRedirect(reverse("home") + "#contact")

    # Combine both contexts
    context = {**data, **contact_context}

    return render(request, "home.html", context)
