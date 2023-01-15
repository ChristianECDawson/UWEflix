from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view()),
    path('create_booking', views.create_booking, name='create_booking'),
    path('bookings', views.BookingView.as_view() )
]
