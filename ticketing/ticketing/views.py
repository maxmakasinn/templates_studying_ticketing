from django.shortcuts import render
from ticketing.models import Ticket


def index(request):
    return render(request, "index.html")


def submit(request):
    new_ticket = Ticket(submitter="Test User", body="Help, I need help with bug!!!")
    new_ticket.save()
    return render(request, "submit.html")


def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": all_tickets})
