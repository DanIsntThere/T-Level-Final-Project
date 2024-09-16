from django.contrib import admin
from .models import ContactUs, Profile, Booking, Hotel
from django.contrib.auth.models import User
admin.site.register(ContactUs)
admin.site.register(Profile)
admin.site.register(Booking)
admin.site.register(Hotel)
class ProfileInLine(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):
    model = UserField = ["username","first_name","last_name","email"]
    inlines = [ProfileInLine]
admin.site.unregister(User)
admin.site.register(User, UserAdmin)