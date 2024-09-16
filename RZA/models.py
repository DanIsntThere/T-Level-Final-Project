from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    num_adult_tickets = models.IntegerField(default=0)
    num_child_tickets = models.IntegerField(default=0)
    num_senior_tickets = models.IntegerField(default=0)
    def total_price(self):
        adult_price=10
        child_price= 5 # Sets the price for the tickets
        senior_price=8
        return (self.num_adult_tickets * adult_price) + (self.num_child_tickets*child_price)+(self.num_senior_tickets*senior_price)
        #Calculates the total price 
class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    price = models.IntegerField()    
    days = models.IntegerField(default=0)
    def __str__(self):
        return f"Date:{self.date} Price:{self.price} Days:{self.days}"

class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    cardNum = models.CharField(max_length=20, blank=True)
    nameOnCard = models.CharField(max_length=50,blank=True)
    expirationDate = models.CharField(max_length=10,blank=True)
    loyaltyPoints = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} has firstname: {self.user.first_name} and email address: {self.user.email}"

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile,sender=User)

    
