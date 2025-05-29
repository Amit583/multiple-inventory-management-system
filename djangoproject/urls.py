"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# """
from django.contrib import admin
from django.urls import include, path
from stockmgmt import views
from stockmgmt.views import dashboard,get_chart_data

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('list_location_master/', views.list_location_master, name='list_location_master'),
    path('add_location_master/', views.add_location_master, name='add_location_master'),
    path('update_location_master/<int:pk>/', views.update_location_master, name='update_location_master'),
    path('delete_location_master/<int:pk>/', views.delete_location_master, name='delete_location_master'),
    
    path('list_ssd/', views.list_ssd, name='list_ssd'),
    path('add_ssd/', views.add_ssd, name='add_ssd'),
    path('update_ssd/<int:pk>/', views.update_ssd, name='update_ssd'),
    path('delete_ssd/<int:pk>/', views.delete_ssd, name='delete_ssd'),
    
    path('list_dtlt/', views.list_dtlt, name='list_dtlt'),
    path('add_dtlt/', views.add_dtlt, name='add_dtlt'),
    path('admin/',views.admin, name='admin'),
    path('add_dtlt/list_dtlt/', views.list_dtlt, name='list_dtlt'),
    path('update_dtlt/<int:pk>/', views.update_dtlt, name='update_dtlt'),
    path('delete_dtlt/<int:pk>/', views.delete_dtlt, name='delete_dtlt'),
    
    path('list_dtltotnetwork/', views.list_dtltotnetwork, name='list_dtltotnetwork'),
    path('add_dtltotnetwork/', views.add_dtltotnetwork, name='add_dtltotnetwork'),
    path('update_dtltotnetwork/<int:pk>/', views.update_dtltotnetwork, name='update_dtltotnetwork'),
    path('delete_dtltotnetwork/<int:pk>/', views.delete_dtltotnetwork, name='delete_dtltotnetwork'),
    
    path('list_dtltretired/', views.list_dtltretired, name='list_dtltretired'),
    path('add_dtltretired/', views.add_dtltretired, name='add_dtltretired'),
    path('update_dtltretired/<int:pk>/', views.update_dtltretired, name='update_dtltretired'),
    path('delete_dtltretired/<int:pk>/', views.delete_dtltretired, name='delete_dtltretired'),
    
    path('list_printer/', views.list_printer, name='list_printer'),
    path('add_printer/', views.add_printer, name='add_printer'),
    path('update_printer/<int:pk>/', views.update_printer, name='update_printer'),
    path('delete_printer/<int:pk>/', views.delete_printer, name='delete_printer'),
    
    path('list_vcprojectorstv/', views.list_vcprojectorstv, name='list_vcprojectorstv'),
    path('add_vcprojectorstv/', views.add_vcprojectorstv, name='add_vcprojectorstv'),
    path('update_vcprojectorstv/<int:pk>/', views.update_vcprojectorstv, name='update_vcprojectorstv'),
    path('delete_vcprojectorstv/<int:pk>/', views.delete_vcprojectorstv, name='delete_vcprojectorstv'),
    
    path('list_ramdetails/', views.list_ramdetails, name='list_ramdetails'),
    path('add_ramdetails/', views.add_ramdetails, name='add_ramdetails'),
    path('update_ramdetails/<int:pk>/', views.update_ramdetails, name='update_ramdetails'),
    path('delete_ramdetails/<int:pk>/', views.delete_ramdetails, name='delete_ramdetails'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.backends.default.urls')),

    # path('search/',views.search, name='search'),

    path('dashboard/', dashboard, name='dashboard'),
    path('chart_data/', get_chart_data, name='chart_data'),


    # path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
]
