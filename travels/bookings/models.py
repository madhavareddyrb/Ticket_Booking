from django.db import models

# Create your models here.
class Bus(models.Model):
  bus_name = models.CharField(max_length = 100)
  bus_number = models.CharField(max_length = 20, unique = True)
  origin = models.CharField(max_length =50)
  destination = models.CharField(max_length = 50)
  price = models.DecimalField(max_digits = 8, decimal_places = 2)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  Features = models.TextField()

  def __str__(self):
    return f"{self.bus_name} {self.bus_number} {self.origin} {self.destination}"
  
class Seat(models.Model):
  bus = models.ForeignKey('Bus',on_delete = models.CASCADE, related_name = 'seats')
  seat_number = models.CharField(max_length=20, unique = True)
  is_booked = models.BooleanField(default = False)

  def __str__(self):
    return f"{self.bus} {self.seat_number} {self.is_booked}"
