from django.contrib import admin
from .models import Viewing, Booking, Rating, Film

admin.site.register(Viewing)
admin.site.register(Booking)
admin.site.register(Rating)
admin.site.register(Film)
