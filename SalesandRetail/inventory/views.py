from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.views import User,username
# Create your views here.
@login_required(login_url='login')
def Inventory(request):
    return render(request,'inventory/inventory.html')

@login_required(login_url='login')
def Dashboard(request):
    return render(request,'inventory/dashboard.html')