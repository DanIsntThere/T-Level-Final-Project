from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.

def login_user(request):
    if request.method =="POST":#If form has been submitted
        username = request.POST['username']#Gets values from
        password = request.POST['password']#form
        user = authenticate(request, username=username, password=password)#Checks if user exists
        if user is not None:#If it does 
            login(request, user)#Logs them in
            messages.success(request,("You are logged in"))#Message displayed
            return redirect('RZA:home')#Sent to home page
        else:
            messages.success(request,("There was an error logging in"))
            return redirect('users:login_user')#Else message appears and page reloads
    else:
        return render(request, 'login.html',{})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)#Gets info from form
        if form.is_valid():#Checks if it's valid
            form.save()#Saves the information
            username = form.cleaned_data['username']#Gets the username
            password = form.cleaned_data['password1']#and password
            user = authenticate(username = username, password=password)#then creates the user
            login(request, user)#and logs the user in
            messages.success(request, ("Registration complete!"))#Displays this message
            return redirect('RZA:home')#Sends them to the home page
    else:
        form = RegisterUserForm()#If the form hasn't been submitted the form will display
    return render(request, 'register_user.html',{'form':form})

def logout_user(request):
    logout(request)
    #messages.add_message(request,messages.INFO,"You have been logged out")
    messages.success(request, ("You have been logged out"))
    return redirect('RZA:home')