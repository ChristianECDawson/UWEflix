from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Screen(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.number

class Rating(models.Model):
    age_rating = models.CharField(max_length=16)

    def __str__(self):
        return self.age_rating

class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    age_rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.title

class Viewing(models.Model):
    film = models.ForeignKey(Film, default=1, on_delete=models.CASCADE)
    start_time = models.TimeField(default=datetime.time(20,00))

    def __str__(self):
        return f'{self.film} - {self.start_time}'

class Booking(models.Model):
     viewing = models.ForeignKey(Viewing, default=1, on_delete=models.CASCADE)
     customer = models.ForeignKey(User, on_delete=models.CASCADE)
     qty = models.IntegerField(default = 10, validators=[
            MaxValueValidator(100),
            MinValueValidator(10)
        ])

     def get_absolute_url(self):
        return reverse('bookings')