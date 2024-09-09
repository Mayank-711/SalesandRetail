"""
URL configuration for SalesandRetail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views
from inventory import views as iviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('logout/',views.LogoutPage,name ='logout'),
    path('dashboard/',iviews.salesDashboard,name='dashboard'),
    path('inventory/',iviews.inventory,name='inventory'),
    path('sales/',iviews.SalesPage,name='sales'),
    path("ChangePassword/<token>/",views.ChangePassword,name="ChangePassword"),
    path("ForgotPassword",views.ForgotPassword,name="ForgotPassword"),
    path("profile/",views.ProfilePage,name="profile"),
    path("profile/profile_update/",views.profile_update,name="profile_update"),
    path('profile/', views.ProfilePage, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


