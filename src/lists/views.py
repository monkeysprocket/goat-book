from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from lists.forms import ItemForm
from lists.models import Item, List


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html", {"form": ItemForm()})


def new_list(request: HttpRequest) -> HttpResponse:
    form = ItemForm(data=request.POST)
    if form.is_valid():
        nulist = List.objects.create()
        Item.objects.create(text=request.POST["text"], list=nulist)
        return redirect(nulist)
    else:
        return render(request, "home.html", {"form": form})


def view_list(request: HttpRequest, list_id: int) -> HttpResponse:
    our_list = List.objects.get(id=list_id)
    if request.method == "POST":
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST["text"], list=our_list)
            return redirect(our_list)
    else:
        form = ItemForm()
    return render(request, "list.html", {"list": our_list, "form": form})
