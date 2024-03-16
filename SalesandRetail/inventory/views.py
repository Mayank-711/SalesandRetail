from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import *
from django.http import JsonResponse
# Create your views here. 


def inventory(request):
    user = request.user 
    username = user.username
    if request.method=="POST":
        data=request.POST
        P_Type=data.get("typeofproduct")
        p_Name=data.get("nameofproduct")
        P_Brand=data.get("brand")
        P_Stock=data.get("stock")
        R_date=data.get("rdate")
        cost=data.get("costprice")
        Inventory.objects.create(username=username,P_Type=P_Type,p_Name=p_Name,P_Brand=P_Brand,P_Stock=P_Stock,R_date=R_date,cost=cost) 
        return redirect("inventory")
    queryset=Inventory.objects.all()
    context={"Inventory":queryset}
    return render(request,'inventory/inventory.html',context=context)

def Dashboard(request):
    return render(request,'inventory/dashboard.html')

def SalesPage(request):
    user = request.user 
    username = user.username
    producttype = Inventory.objects.filter(username=username).values('P_Type').distinct()
    btype = Inventory.objects.filter(username=username).values('P_Brand').distinct()
    ntype = Inventory.objects.filter(username=username).values('p_Name').distinct()
    context = {'ptypes':producttype,'brandtypes':btype,'pnames':ntype}
    return render(request,'inventory/sales.html',context=context)
