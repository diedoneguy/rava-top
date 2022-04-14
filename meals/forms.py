import django
from .models import Reservation
from django import forms


class ReserveTable(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        