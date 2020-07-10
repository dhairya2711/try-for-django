from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight, Passenger


# Create your views here.
def index(request):
    return render(request, 'index.html', {"Flights": Flight.objects.all()})


def ret(request, flight_id):
    flight_info = Flight.objects.get(id=flight_id)
    in_passengers = Passenger.objects.filter(flight=flight_info).all()
    no_passengers = Passenger.objects.exclude(flight=flight_info).all()

    content = {"Flight": flight_info, "Passengers": in_passengers, "Non_passengers": no_passengers}
    return render(request, 'flight.html', content)


def flight_def(request, flight_id):
    if request.method == "POST":
        id = request.POST["add_p"]
        passenger = Passenger.objects.get(id=id)
        flight = Flight.objects.get(id=flight_id)
        passenger.flight.add(flight)
        return ret(request, flight_id)
    else:
        return ret(request, flight_id)