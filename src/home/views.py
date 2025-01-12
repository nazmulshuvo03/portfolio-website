import json
from pathlib import Path

from django.shortcuts import render


def home(request):
    # Path to the JSON file
    data_file = Path(__file__).resolve().parent.parent / "static/js/data.json"

    # Load JSON data
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        data = {}

    return render(request, "home.html", data)
