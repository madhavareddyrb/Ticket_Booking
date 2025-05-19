from django.contrib import admin
from bookings.models import *

# Register your models here.``
class BusAdmin(admin.ModelAdmin):
  list_display=("bus_name","bus_number",'origin','destination')
admin.site.register(Bus,BusAdmin)
admin.site.register(Seat)
