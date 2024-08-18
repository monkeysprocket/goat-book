from django.http import HttpRequest
from django.shortcuts import render


def home_page(request: HttpRequest):
    return render(
        request,
        "home.html",
        {"new_item_text": request.POST.get("item_text", "")},
    )
