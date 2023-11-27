from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=200)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=200)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=200, blank=True, null=True)  # Field name made lowercase.
    passwrd = models.CharField(db_column='Passwrd', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'



class Admin(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    admin_id = models.IntegerField(db_column='Admin_id', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='Admin_name', max_length=200)  # Field name made lowercase.
    passwrd = models.CharField(db_column='Passwrd', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'

    def __str__(self):
        return self.admin_name

class Location(models.Model):
    location_name = models.CharField(db_column='Location_name', primary_key=True, max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'

    def __str__(self):
        return self.location_name


class Train(models.Model):
    train_no = models.IntegerField(db_column='Train_No', primary_key=True)  # Field name made lowercase.
    name_of_trains = models.CharField(db_column='Name_of_Trains', max_length=512, blank=True, null=True)  # Field name made lowercase.
    off_day = models.CharField(db_column='Off_day', max_length=512, blank=True, null=True)  # Field name made lowercase.
    starting_station = models.CharField(db_column='Starting_Station', max_length=512, blank=True, null=True)  # Field name made lowercase.
    departure_time = models.CharField(db_column='Departure_Time', max_length=512, blank=True, null=True)  # Field name made lowercase.
    arrival_station = models.CharField(db_column='Arrival_station', max_length=512, blank=True, null=True)  # Field name made lowercase.
    arrival_time = models.CharField(db_column='Arrival_Time', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'train'


class Reservation(models.Model):
    reservation_id = models.IntegerField(primary_key=True)
    total_fare = models.IntegerField()
    no_of_ticket = models.IntegerField()
    train_no = models.ForeignKey(Train, null=True, on_delete=models.SET_NULL, db_column='train_no')
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    location_name = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL, db_column='location_name')

    class Meta:
        managed = False
        db_table = 'reservation'


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    payment_method = models.CharField(max_length=200)
    reservation = models.ForeignKey(Reservation, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'payment'



class Seats(models.Model):
    capacity = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=200)  # Field renamed because it was a Python reserved word.
    ticket_price = models.IntegerField()
    train_no = models.ForeignKey(Train, null=True, on_delete=models.SET_NULL, db_column='train_no')

    class Meta:
        managed = False
        db_table = 'seats'



class Station(models.Model):
    station_name = models.CharField(primary_key=True, max_length=200)
    location_name = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL, db_column='location_name')

    class Meta:
        managed = False
        db_table = 'station'

    def __str__(self):
        return self.station_name


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    arrival_time = models.IntegerField(db_column='Arrival_time')  # Field name made lowercase.
    depart_time = models.IntegerField(db_column='Depart_time')  # Field name made lowercase.
    reservation = models.ForeignKey(Reservation, null=True, on_delete=models.SET_NULL)
    train_no = models.ForeignKey(Train, null=True, on_delete=models.SET_NULL, db_column='train_no')

    class Meta:
        managed = False
        db_table = 'ticket'





