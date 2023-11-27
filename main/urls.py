from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Cus1_HomePage/', views.Cus1_HomePage, name='Cus1_HomePage'),
    path('Cus2_LoginPage/', views.Cus2_LoginPage, name='Cus2_LoginPage'),
    path('Cus3_RegisterPage/', views.Cus3_RegisterPage, name='Cus3_RegisterPage'),
    path('Cus5_PaymentOther/', views.Cus5_PaymentOther, name='Cus5_PaymentOther'),
    path('Cus6_PaymentCard/', views.Cus6_PaymentCard, name='Cus6_PaymentCard'),
   
    path('Confirm/', views.Confirm, name='Confirm'),
    path('EndConfirmation/', views.EndConfirmation, name='EndConfirmation'),
    
    path('ticketReservation/', views.ticketReservation, name='ticketReservation'),
    path('TrainInfoTable/', views.TrainInfoTable, name='TrainInfoTable'),
    
    path('Admin1_LoginPage/', views.Admin1_LoginPage, name='Admin1_LoginPage'),
    path('Admin2_HomePage/', views.Admin2_HomePage, name='Admin2_HomePage'),
    path('Admin3_AddTrainPage/', views.Admin3_AddTrainPage, name='Admin3_AddTrainPage'),
    path('Admin4_DeleteTrain/', views.Admin4_DeleteTrain, name='Admin4_DeleteTrain'),
    path('Admin5_AboutUs/', views.Admin5_AboutUs, name='Admin5_AboutUs')

]