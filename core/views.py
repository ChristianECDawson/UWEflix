from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Viewing, Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Viewing
    template_name = 'index.html'

class BookingView(ListView):
    model = Booking
    template_name = 'bookings.html'

def create_booking(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    form = BookingForm
    return render(request, 'create_booking.html', {'form':form})