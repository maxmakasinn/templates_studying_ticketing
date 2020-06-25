from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def submit(request):
    return render(request, "submit.html")


def tickets(request):
    return render(request, "tickets.html")
