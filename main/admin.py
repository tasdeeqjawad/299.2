from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Admin
from .models import Location
from .models import Train
from .models import Reservation
from .models import Payment
from .models import Seats
from .models import Station
from .models import Ticket


admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Location)
admin.site.register(Train)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Seats)
admin.site.register(Station)
admin.site.register(Ticket)
