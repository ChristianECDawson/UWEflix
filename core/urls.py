from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view()),
    path('create_booking', views.CreateBookingView.as_view(), name="create_booking"),
    path('bookings', views.BookingView.as_view(), name="bookings" ),
    path('update_booking/<int:pk>', views.UpdateBookingView.as_view(), name="update_booking" ),
    path('delete_booking/<int:pk>', views.DeleteBookingView.as_view(), name="delete_booking" ),

]
