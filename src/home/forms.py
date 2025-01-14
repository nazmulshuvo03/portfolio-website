import re

from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    test = (forms.CharField(label="Test", max_length=100),)
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"},
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Your Email"}
        ),
        error_messages={
            "required": "Please provide a valid email address",
        },
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your Message",
                "rows": 5,
            }
        ),
        error_messages={
            "required": "Please enter your message",
        },
    )

    def clean_message(self):
        message = self.cleaned_data.get("message", "")

        if re.search(
            r"<script|select|insert|update|delete|drop", message, re.IGNORECASE
        ):
            raise ValidationError("Invalid content detected in the message.")

        # Enforce a minimum length for the message
        if len(message.strip()) < 10:
            raise ValidationError("Message must be at least 10 characters long.")

        return message
