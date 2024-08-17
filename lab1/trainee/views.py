from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def trainee_list(request):
    trainees = [
        {
            "id": 1,
            "name": "nada",
            "age": 23,
            "email": "nada@gmail.com",
            "department": "pyhton",
        },
        {
            "id": 2,
            "name": "mohamed",
            "age": 27,
            "email": "mohamed@gmail.com",
            "department": "python",
        },
        {
            "id": 3,
            "name": "mostafa",
            "age": 27,
            "email": "mostafa@gmail.com",
            "department": "python",
        },
    ]
    context = {}
    context["trainees"] = trainees
    return render(request, "trainee/list.html", context)
    # return HttpResponse("<h1>Trainee List</h1>")


def trainee_create(request):
    # return HttpResponse("<h1>Trainee create</h1>")
    return render(request, "trainee/create.html")


def trainee_update(request, id):
    # return HttpResponse("<h1>Trainee update</h1>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/update.html", context)


def trainee_delete(request, id):
    # return HttpResponse("<h1>Trainee delete</h1>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/delete.html", context)


def trainee_details(request, id):
    # return HttpResponse(f"<h1>Trainee Details: {id}</h1>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/details.html", context)
