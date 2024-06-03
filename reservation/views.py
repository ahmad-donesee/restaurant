from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ReservationForm
from . models import Reserve
# Create your views here.

def reserve(request):
    reserve_form=ReservationForm()
    if request.method=="POST":
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            return redirect("food:foodlist")
        else:
            return HttpResponse("invalid data")
    else:
        reserve_form=ReservationForm()
    
        context={
            "form":reserve_form
        }
        return render(request,"reservation/reserve.html",context)