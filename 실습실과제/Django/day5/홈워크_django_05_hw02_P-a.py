from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

    class meta:
        model = Reservation
        fields = '__all__'