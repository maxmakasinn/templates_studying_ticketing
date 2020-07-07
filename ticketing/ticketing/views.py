from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ticketing.models import Ticket


def index(request):
    return render(request, "index.html")


def submit(request):
    if request.method == "POST":
        username = request.POST.get("username")
        body = request.POST.get("body")
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse("Successfully submitted ticket!")
    return render(request, "submit.html")


def tickets_raw(request):
    all_tickets = list(Ticket.objects.values())
    return JsonResponse(all_tickets, safe=False)

def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": all_tickets})


def ticket(request, ticket_id):
    selected_ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, "ticket.html", {"ticket": selected_ticket})
