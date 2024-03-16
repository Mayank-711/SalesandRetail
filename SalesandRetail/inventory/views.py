from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import *
# Create your views here. 
def inventory(request):
    if request.method=="POST":
        data=request.POST
        P_Type=data.get("typeofproduct")
        p_Name=data.get("nameofproduct")
        P_Brand=data.get("brand")
        P_Stock=data.get("stock")
        R_date=data.get("rdate")
        cost=data.get("costprice")
        Inventory.objects.create(P_Type=P_Type,p_Name=p_Name,P_Brand=P_Brand,P_Stock=P_Stock,R_date=R_date,cost=cost) 
        return redirect("inventory")
    queryset=Inventory.objects.all()
    context={"Inventory":queryset}
    return render(request,'inventory/inventory.html',context=context)

def Dashboard(request):
    return render(request,'inventory/dashboard.html')