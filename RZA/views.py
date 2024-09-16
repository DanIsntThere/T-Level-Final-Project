from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Booking, Profile, Hotel
from RZA.forms import ContactForm, ProfileForm,MyUserChangeForm
from users.forms import RegisterUserForm


def home(request):
    return render(request,'home.html')


def information(request):
    if request.method == "POST":
        form = ContactForm(request.POST)#Gets form 
        if form.is_valid():#Checks if valid
            form.save()#saves
            messages.success(request,("Message sent"))#User feedback for accessibility
    form = ContactForm
    return render(request,'information.html',{'form':form})


def tickets(request):
    if request.method == 'POST':
        date = request.POST['date']#Gets info from form
        num_adult_tickets = int(request.POST.get('num_adult_tickets', 0))
        num_child_tickets = int(request.POST.get('num_child_tickets', 0))
        num_senior_tickets = int(request.POST.get('num_senior_tickets', 0))
        price = int(request.POST['hidden_Price'])
        
        booking = Booking.objects.create(#Creates booking from form
            user=request.user,
            date=date,
            num_adult_tickets=num_adult_tickets,
            num_child_tickets=num_child_tickets,
            num_senior_tickets=num_senior_tickets
        )
        profile = Profile.objects.get(user=request.user)
        profile = request.user.profile#gets users profile info
        current = profile.loyaltyPoints#gets their current loyalty points
        profile.loyaltyPoints = current + (price*10)#Adds more 
        profile.save()#Saves 
        messages.success(request,("Zoo Tickets Booked"))
        return redirect('RZA:profile')
    else:
        return render(request, 'tickets.html')


def hotel(request):
    if request.method=='POST':
        """ date = request.POST['date']
        price = int(request.POST['hidden_Price'])       This is my date validation
        days = int(request.POST['days'])                It doesn't work :(
        type(date)
        format = "%Y-%m-%d"
        dat = datetime.strptime(date, format)
        print(dat)
        print(timezone.now()) 
        
        current_date = timezone.now()
        #if dat> current_date:
        #    messages.success(request,("Invalid date, try again"))
        #    return redirect('RZA:hotel')"""
        try:
            date = request.POST['date']
            price = int(request.POST['hidden_Price'])#Gets values from form
            days = int(request.POST['days'])
        except: 
            messages.success(request,('You must fill in all inputs'))
            return redirect('RZA:hotel')#error handling 
            
        hotel = Hotel.objects.create(#Creates object
            user=request.user,
            date=date,
            price=price,
            days=days
        )
        profile = Profile.objects.get(user=request.user)
        profile = request.user.profile#gets users profile info
        current = profile.loyaltyPoints#gets their current loyalty points
        profile.loyaltyPoints = current + (price*10)#Adds more 
        profile.save()#Saves 
        messages.success(request,("Hotel Room Booked"))
        return redirect('RZA:profile')
    else:
        return render(request, 'hotel.html')


def profile(request): 
    if request.user.is_authenticated:#Checks if user is signed in
        current_user = User.objects.get(id=request.user.id)#Gets the user's id
        userForm = MyUserChangeForm(request.POST or None, instance=current_user)#Gets their information from the registration form

        profile_user = Profile.objects.get(user__id=request.user.id)#Gets the users profile information
        profileform= ProfileForm(request.POST or None, request.FILES or None, instance=profile_user)#Gets the profile form

        if profileform.is_valid() and userForm.is_valid():#If both forms are valid
            userForm.save()#                               It will save them both
            profileform.save()
            messages.success(request, "Your information has been saved successfully")#Message will appear
            return redirect('RZA:profile')#reload the page

        bookings = Booking.objects.filter(user=request.user)#Gets the users bookings 
        hotel = Hotel.objects.filter(user=request.user)     # for the zoo tickets and hotel
        profile = Profile.objects.filter(user=request.user)# And also the users profile information
        return render(request, "profile.html", {'userForm':userForm,'profileform':profileform,'bookings':bookings,'hotel':hotel,'profile':profile})
    else:
        return render(request,"profile.html")


def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
     #^Gets booking info
    price = booking.total_price()
    points = price *10 #Calcs amount of points
    profile = Profile.objects.get(user=request.user)
    profile = request.user.profile#Gets user details
    current = profile.loyaltyPoints
    profile.loyaltyPoints = current -points#Removes points from booking
    profile.save()#Saves
    booking.delete()#Deletes booking
    messages.success(request, "Your booking has been cancelled")
    return redirect('RZA:profile')


def cancel_hotel(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    price = hotel.price
    points = price *10 #Calcs amount of points
    profile = Profile.objects.get(user=request.user)
    profile = request.user.profile#Gets user details
    current = profile.loyaltyPoints
    profile.loyaltyPoints = current -points#Removes points from booking
    profile.save()#Saves
    hotel.delete()
    messages.success(request, "Your booking has been cancelled")
    return redirect('RZA:profile')


def terms(request):
    return render(request, 't&cs.html')

def policy(request):
    return render(request, 'policy.html')

def schoolTrip(request):
    return render(request, 'schoolTrip.html')
