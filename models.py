# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_id = models.IntegerField(db_column='Admin_id', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='Admin_name', max_length=200)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200)  # Field name made lowercase.
    customer = models.ForeignKey('Customer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=10)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=10)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=10, blank=True, null=True)  # Field name made lowercase.
    age = models.JSONField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    passwrd = models.CharField(db_column='Passwrd', max_length=10)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Location(models.Model):
    location_name = models.CharField(db_column='Location_name', primary_key=True, max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    payment_method = models.CharField(max_length=200)
    reservation = models.ForeignKey('Reservation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment'


class Reservation(models.Model):
    reservation_id = models.IntegerField(primary_key=True)
    total_fare = models.IntegerField()
    no_of_ticket = models.IntegerField()
    train_no = models.ForeignKey('Train', models.DO_NOTHING, db_column='train_no')
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    location_name = models.ForeignKey(Location, models.DO_NOTHING, db_column='location_name')

    class Meta:
        managed = False
        db_table = 'reservation'


class Seats(models.Model):
    capacity = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=200)  # Field renamed because it was a Python reserved word.
    ticket_price = models.IntegerField()
    train_no = models.ForeignKey('Train', models.DO_NOTHING, db_column='train_no')

    class Meta:
        managed = False
        db_table = 'seats'


class Station(models.Model):
    station_name = models.CharField(primary_key=True, max_length=200)
    location_name = models.ForeignKey(Location, models.DO_NOTHING, db_column='location_name')

    class Meta:
        managed = False
        db_table = 'station'


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    arrival_time = models.IntegerField(db_column='Arrival_time')  # Field name made lowercase.
    depart_time = models.IntegerField(db_column='Depart_time')  # Field name made lowercase.
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING)
    train_no = models.ForeignKey('Train', models.DO_NOTHING, db_column='train_no')

    class Meta:
        managed = False
        db_table = 'ticket'


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
