from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Customer, Train, Admin, Seats, Reservation, Ticket, Station, Payment, Location




# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

def Cus2_LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('uname')
        password = request.POST.get('pword')

        try:
            customer = Customer.objects.get(email=email, password=password)
            # Successful login, redirect 
            return redirect('main:Cus1_HomePage')  # Adjust the URL for the next page
        except Customer.DoesNotExist:
            # Invalid credentials, show an error message
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        # This part is executed for GET requests or when the form is not submitted
        return render(request, 'main/Cus2_LoginPage.html')

    return render(request, 'main/Cus2_LoginPage.html', {})

def Cus3_RegisterPage(request):
    if request.method == 'POST':
        email = request.POST.get('mailid')
        password = request.POST.get('pword')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone_number = request.POST.get('phoneno')
        
        # Create and save a new customer
        customer = Customer(email=email, passwrd=password, fname=first_name, lname=last_name, phone_number=phone_number)
        customer.save()
        # Redirect to a success page or another URL
        return redirect('main/Cus2_LoginPage.html') #url for the next page should be here
    return render(request, "main/Cus3_RegisterPage.html", {})

def Cus1_HomePage(request):
    return render(request, "main/Cus1_HomePage.html", {})


def Admin1_LoginPage(request):
    if request.method == 'POST':
        admin_id = request.POST('id')
        password = request.POST('pword')

        try:
            admin = Admin.objects.get(Admin_id=admin_id, password=password)
            # Successful login, redirect 
            return redirect('main/Admin2_HomePage')  # Adjust the URL for the next page
        except Admin.DoesNotExist:
            # Invalid credentials, show an error message
            messages.error(request, 'Invalid credentials. Please try again.')

    # This part is executed for GET requests or when the form is not submitted
    return render(request, 'Admin1_LoginPage.html')
    #return render(request, "Admin1_LoginPage.html", {})

def Admin2_HomePage(request):
    return render(request, "main/Admin2_HomePage.html", {})

def Admin3_AddTrainPage(request):
    if request.method == 'POST':
        train_number = request.POST.get('trainno')
        train_name = request.POST.get('trainname')
        from_station = request.POST.get('fromstation')
        to_station = request.POST.get('tostation')
        available = request.POST.get('available')
        fare = request.POST.get('fare')

        # Create Train and Seats objects
        train = Train.objects.create(train_no=train_number, name_of_trains=train_name, starting_station=from_station, arrival_station=to_station)
        Seats.objects.create(ticket_price=fare, train_no=train_number)
        train.save()

        # Add your train addition logic here
        return f'Train Number: {train_number}, Train Name: {train_name}, From: {from_station}, To: {to_station}, Available: {available}, Fare: {fare}'

    return render(request, 'Admin2_HomePage.html')
    # return render(request, 'Admin2_HomePage.html')  # Currently inactive this line but after successful adding it should go back to admin home
    return render(request, "main/Admin3_AddTrainPage.html", {})
def Admin5_AboutUs(request):
    return render(request, "main/Admin5_AboutUs.html", {})

def TrainInfoTable(request):
    return render(request, "main/TrainInfoTable.html", {})

def Confirm(request):
    return render(request, "main/Confirm.html", {})

def Admin4_DeleteTrain(request):
    if request.method == 'POST':
    
        train_number = request.POST.get('trainno')

        train = get_object_or_404(Train, train_no=train_number)# finds the specified object from the table

        train.delete()
        # Redirect to a success page or another URL
        return redirect('Admin2_HomePage.html')
    return render(request, "main/Admin4_DeleteTrain.html", {})


def ticketReservation(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        number_of_seats = request.POST.get('seats')
        passengers = request.POST.get('passengers')
        trainNumber =request.POST.get('trainNumber')
        date = request.POST.get('date')
        seating_preference = request.POST.get('seating_preference')
        coach_type = request.POST.get('coach_type')
        

        # Convert train_number and time_str to the appropriate types
        #train_number = int(dropdown.split()[0][1:]) if dropdown else None
        #time_str = dropdown.split("(Departure time: ")[1].replace(")", "")
        #departure_time = datetime.strptime(time_str, "%H:%M").time() if time_str else None

        # Fetch data from the database
        price = Seats.objects.filter(train__train_no=train_number).values_list('ticket_price', flat=True).first()
        available = Seats.objects.filter(train__train_no=train_number).values_list('capacity', flat=True).first()

        if number_of_seats > available:
            # Output an error message
            return render(request, 'yourapp/error.html')

        else:# Create objects in the database
            fare = price * int(number_of_seats)
            reservation = Reservation.objects.create(total_fare=fare, no_of_tickets=number_of_seats, train_no=train_number, customer=customer_id, location_name='#') #NO LOCATION PASSED
            ticket = Ticket.objects.create(depart_time=departure_time, reservation=reservation)
            Seats.objects.filter(train__train_no=train_number).update(capacity=models.F('capacity') - number_of_seats)

            # Successful message should pop-up

            context = {
                'full_name': name,
                'phone_number': phone,
                'train_number': trainNumber,
                'fare': fare,  
                'coach_type': coach_type,  # Replace with actual data
                'seating_preference': seating_preference,  # Replace with actual data
                'date': date,  # Replace with actual data
                'passenger_count': passengers,  
                'number_of_seats': number_of_seats  
            }
            return render(request, 'Confirm.html', context)

        #return render(request, 'yourapp/success.html')
    return render(request, "main/ticketReservation.html", {})

def EndConfirmation(request):
    return render(request, "main/EndConfirmation.html", {})

def Cus5_PaymentOther(request):
    return render(request, "main/Cus5_PaymentOther.html", {})

def Cus6_PaymentCard(request):
    return render(request, "main/Cus6_PaymentCard.html", {})
