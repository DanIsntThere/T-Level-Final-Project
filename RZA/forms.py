from django.forms import ModelForm
from django import forms
from .models import ContactUs, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('image', )

class MyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')