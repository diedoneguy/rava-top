from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
# Create your views here.
def reserve_table(request):
    reserve_table = ReservationForm()
    if reserve_table == 'POST':
        reserve_table = ReservationForm(request)
        if reserve_table.is_valid():
            reserve_table.save()
            reserve_table = ReservationForm
    
    context = {
        'form': reserve_table
    }
    
    return render(request, '', context)