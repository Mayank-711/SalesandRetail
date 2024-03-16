from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.views import LoginPage
# Create your views here. 
def Inventory(request):
    return render(request,'inventory/inventory.html')

def Dashboard(request):
    return render(request,'inventory/dashboard.html')