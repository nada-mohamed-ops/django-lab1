from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def account_list(request):
    accounts = [
        {"id": 1, "email": "nada@gmail.com", "password": "mm123"},
        {"id": 2, "email": "mohamed@gmail.com", "password": "456456"},
        {"id": 3, "email": "mostafa@gmail.com", "password": "453288"},
    ]
    context = {}
    context["accounts"] = accounts
    return render(request, "account/list.html", context)
    # return HttpResponse("<h1>account List</h1>")


def account_create(request):
    # return HttpResponse("<h1>account create</h1>")
    return render(request, "account/create.html")


def account_update(request, id):
    # return HttpResponse("<h1>account update</h1>")
    context = {}
    context = {"id": id}
    return render(request, "account/update.html", context)


def account_delete(request, id):
    # return HttpResponse("<h1>account delete</h1>")
    context = {}
    context = {"id": id}
    return render(request, "account/delete.html", context)


def account_details(request, id):
    # return HttpResponse(f"<h1>account Details: {id}</h1>")
    context = {}
    context = {"id": id}
    return render(request, "account/details.html", context)
