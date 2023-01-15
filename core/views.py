from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Viewing, Booking
from .forms import BookingForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Viewing
    template_name = 'index.html'

class BookingView(ListView):
    model = Booking
    template_name = 'bookings.html'

class CreateBookingView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'create_booking.html'

class UpdateBookingView(UpdateView):
    model = Booking
    template_name = 'update_booking.html'
    fields = '__all__'

class DeleteBookingView(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('bookings')
 