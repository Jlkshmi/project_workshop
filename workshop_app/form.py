from django import forms
from django.contrib.auth.forms import UserCreationForm

from workshop_app.models import Login, Customer, Workmanager


# login
class Login_Form(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

# for customerlogin
class Customer_Form(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','contact_no','email','address','lisence_no','vehicle_model')

class Workmanager_Form(forms.ModelForm):
    class Meta:
        model=Workmanager
        fields=('name','contact_no','email','address','emp_id')

