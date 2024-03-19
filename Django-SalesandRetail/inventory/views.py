from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import *
from django.http import JsonResponse
from django.db.models import F,Q,Sum
from django.contrib import messages
from datetime import datetime, timedelta
# import plotlib
# Create your views here. 



def salesDashboard(request):
    user = request.user
    print(user)
    username = user.username
    thirty_days_ago = datetime.now() - timedelta(days=30)
    print(username)
    print(thirty_days_ago)
    sales_30d_total = Sales.objects.filter(PS_date__gte=thirty_days_ago,username=username).aggregate(total_sales_30d=Sum('SellingPrice'))
    context = {"total_sales_30d":sales_30d_total}
    return render(request,'inventory/dashboard.html',context=context)


def inventory(request):
    user = request.user 
    username = user.username
    if request.method == "POST":
        data = request.POST
        P_Type = data.get("typeofproduct")
        p_Name = data.get("nameofproduct")
        P_Brand = data.get("brand")
        P_Stock = data.get("stock")
        R_date = data.get("rdate")
        cost = data.get("costprice")
        P_Size = data.get('shoesize')
        existing_inventory = Inventory.objects.filter(username=username, P_Type=P_Type, p_Name=p_Name, P_Brand=P_Brand, P_Size=P_Size).first()
        if existing_inventory:
            existing_inventory.P_Stock += int(P_Stock)
            existing_inventory.R_date = R_date
            existing_inventory.cost = cost
            existing_inventory.save()
            messages.success(request, f'Inventory for {p_Name} updated successfully.')
        else:
            Inventory.objects.create(username=username, P_Type=P_Type, p_Name=p_Name, P_Brand=P_Brand, P_Stock=P_Stock, R_date=R_date, cost=cost, P_Size=P_Size)
            messages.success(request, f'New inventory for {p_Name} added successfully.')
        return redirect("inventory")
    
    queryset = Inventory.objects.filter(username=username).order_by('-R_date')
    context = {"Inventory": queryset}
    return render(request, 'inventory/inventory.html', context=context)

def SalesPage(request):
    user = request.user 
    username = user.username
    producttype = Inventory.objects.filter(username=username).values('P_Type').distinct()
    btype = Inventory.objects.filter(username=username).values('P_Brand').distinct()
    ntype = Inventory.objects.filter(username=username).values('p_Name').distinct()
    ssize = Inventory.objects.filter(username=username).values('P_Size').distinct()
    if request.method == "POST":
        data = request.POST
        customer_name = data.get('cname')
        customer_email = data.get('cmail')
        PS_Type = data.get("stype")
        PS_Name = data.get("sname")
        PS_Brand = data.get("sbrand")
        QuantitySold = data.get("scount")
        PS_date = data.get("sellingDate")
        SellingPrice = data.get("sellingPrice")
        PS_Size = data.get('Ssize')
        # Create a new sales record
        Sales.objects.create(
            username=username,
            PS_Type=PS_Type,
            PS_Name=PS_Name,
            PS_Brand=PS_Brand,
            QuantitySold=QuantitySold,
            PS_Date=PS_date,
            SellingPrice=SellingPrice,
            customer_name=customer_name,
            customer_email=customer_email,
            PS_Size=PS_Size
        ) 
        
        # Update the inventory
        Inventory.objects.filter(username=username, P_Type=PS_Type, P_Brand=PS_Brand, p_Name=PS_Name, P_Size=PS_Size).update(
            P_Stock=F('P_Stock') - int(QuantitySold)
        )
        
        messages.success(request, f'Sales for {PS_Name} added successfully.')
        
        return redirect("sales")
    
    qset = Sales.objects.all().order_by('-PS_Date')[:25]
    context = {'ptypes': producttype, 'brandtypes': btype, 'pnames': ntype, "Sales": qset, "Ssize": ssize}
    return render(request, 'inventory/sales.html', context=context)