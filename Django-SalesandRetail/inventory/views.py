from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import *
from django.http import JsonResponse
from django.db.models import F,Q,Sum,Avg
from django.contrib import messages
from datetime import datetime, timedelta
from decimal import Decimal
import plotly.graph_objs as go
# import plotlib
# Create your views here. 



def salesDashboard(request):
    user = request.user
    username = user.username
    thirty_days_ago = datetime.now() - timedelta(days=30)
    

    sales_30d_total = Sales.objects.filter(PS_Date__gte=thirty_days_ago, username=username).aggregate(total_sales_30d=Sum('SellingPrice'))

    cost_price_30d_total = Inventory.objects.filter(R_date__gte=thirty_days_ago, username=username).annotate(total_cost=F('cost') * F('P_Stock')).aggregate(total_cost_price_30d=Sum('total_cost'))

    profit_30d_total = sales_30d_total['total_sales_30d'] - cost_price_30d_total['total_cost_price_30d']

    total_items_in_stock = Inventory.objects.filter(username=username).aggregate(total_items=Sum('P_Stock'))

    distinct_customers_30d_count = Sales.objects.filter(PS_Date__gte=thirty_days_ago, username=username).values('customer_name').distinct().count()
    
    avg_selling_price_30d = Sales.objects.filter(PS_Date__gte=thirty_days_ago, username=username).aggregate(avg_selling_price_30d=Avg('SellingPrice'))
    avg_selling_price_30d = avg_selling_price_30d['avg_selling_price_30d']
    avg_selling_price_30d = "{:.2f}".format(avg_selling_price_30d)

    sales_data = Sales.objects.filter(PS_Date__gte=thirty_days_ago,username=username)
    product_sales = {}
    for sale in sales_data:
        product_name = sale.PS_Name
        quantity_sold = sale.QuantitySold
        if product_name in product_sales:
            product_sales[product_name] += quantity_sold
        else:
            product_sales[product_name] = quantity_sold
    top_5_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
    product_names = [item[0] for item in top_5_products]
    sales_quantities = [item[1] for item in top_5_products]
    graph_data = [go.Bar(x=product_names, y=sales_quantities)]
    graph_layout = go.Layout(title='Top 5 Products Sold in Last 30 Days', xaxis=dict(title='Product'), yaxis=dict(title='Quantity Sold'))
    graph_figure = go.Figure(data=graph_data, layout=graph_layout)
    graph_html = graph_figure.to_html(full_html=False, default_height=500, default_width=700)

    inventory_items = Inventory.objects.filter(username=username)
    brand_counts = {}
    total_items = 0
    for item in inventory_items:
        brand = item.P_Brand
        if brand in brand_counts:
            brand_counts[brand] += 1
        else:
            brand_counts[brand] = 1
        total_items += 1
    brand_percentage = {brand: (count / total_items) * 100 for brand, count in brand_counts.items()}
    labels = list(brand_percentage.keys())
    values = list(brand_percentage.values())
    trace = go.Pie(labels=labels, values=values, hole=0.3)
    layout = go.Layout(title='Brand-wise Inventory Distribution')
    fig = go.Figure(data=[trace], layout=layout)
    graph1_html = fig.to_html(full_html=False)


    context = {
        "total_sales_30d": sales_30d_total,
        "total_cost_price_30d": cost_price_30d_total,
        "profit_30d_total": profit_30d_total,
        "total_item_in_stock":total_items_in_stock,
        "distinct_customers_30d_count": distinct_customers_30d_count,
        "avg_selling_price_30d": avg_selling_price_30d,
        'graph_html': graph_html,
        'graph1_html':graph1_html,
    }
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