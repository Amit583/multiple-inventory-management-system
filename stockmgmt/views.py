from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import (
    LocationMaster, SSD, DTLT, DTLTOTNetwork, DTLTRetired,
    Printer, VCProjectorsTV, RAMDetails
)
from .forms import *
# (
#     LocationMasterForm, SSDForm, DTLTForm, DTLTOTNetworkForm, DTLTRetiredForm,
#     PrinterForm, VCProjectorsTVForm, RAMDetailsForm, LocationMasterSearchForm,
#     SSDSearchForm, DTLTSearchForm, DTLTOTNetworkSearchForm, DTLTRetiredSearchForm,
#     PrinterSearchForm, VCProjectorsTVSearchForm, RAMDetailsSearchForm
# )
from django.db.models import Count, Case, When, IntegerField
from django.utils import timezone
from django.http import JsonResponse
from django.core.cache import cache
from django.shortcuts import render


@login_required
def home(request):
    title = "Welcome: This is the home page"

    # Initialize an empty dictionary to store the filtered querysets
    inventories = {}

    # DTLT
    if request.user.has_perm('stockmgmt.list_dtlt.html'):  # Update app_name to the actual app name
        inventories['DTLT'] = DTLT.objects.filter(assigned_to_user=request.user.username)
    else:
        inventories['DTLT'] = DTLT.objects.none()

    # SSD
    if request.user.has_perm('stockmgmt.list_ssd.html'):
        inventories['SSD'] = SSD.objects.filter(created_by=request.user.username)
    else:
        inventories['SSD'] = SSD.objects.none()

    # Printer
    if request.user.has_perm('stockmgmt.list_printer.html'):
        inventories['Printer'] = Printer.objects.filter(created_by=request.user.username)
    else:
        inventories['Printer'] = Printer.objects.none()

    # LocationMaster
    if request.user.has_perm('stockmgmt.list_location_master'):
        inventories['LocationMaster'] = LocationMaster.objects.filter(timestamp__gte=request.user.date_joined)
    else:
        inventories['LocationMaster'] = LocationMaster.objects.none()

    # VCProjectorsTV
    if request.user.has_perm('stockmgmt.list_vcprojectorstv.html'):
        inventories['VCProjectorsTV'] = VCProjectorsTV.objects.filter(created_by=request.user.username)
    else:
        inventories['VCProjectorsTV'] = VCProjectorsTV.objects.none()

    # RAMDetails
    if request.user.has_perm('stockmgmt.list_ramdetails.html'):
        inventories['RAMDetails'] = RAMDetails.objects.filter(created_by=request.user.username)
    else:
        inventories['RAMDetails'] = RAMDetails.objects.none()

    context = {
        "title": title,
        "inventories": inventories,
    }

    return render(request, "home.html", context)




# Home Page View
@login_required
def home(request):
    title = "Welcome: This is the home page"
    context = {"title": title}
    return render(request, "home.html", context)

# Generic Add Item View
@login_required
def add_item(request, form_class, success_message, redirect_view):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect(redirect_view)
    else:
        form = form_class()
    
    context = {"form": form, "title": "ADD ITEM"}
    return render(request, "add_items.html", context)

# Generic Update Item View
@login_required
def update_item(request, pk, model, form_class, success_message, redirect_view):
    queryset = get_object_or_404(model, pk=pk)
    form = form_class(instance=queryset)
    if request.method == 'POST':
        form = form_class(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect(redirect_view)
    
    context = {'form': form}
    return render(request, 'add_items.html', context)

# Generic Delete Item View
@login_required
def delete_item(request, pk, model, redirect_view):
    queryset = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.warning(request, 'Item has been deleted')
        return redirect(redirect_view)
    return render(request, 'delete.html')

# List Location Master
@login_required
def list_location_master(request):
    form = LocationMasterSearchForm(request.GET or None)
    queryset = LocationMaster.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        for field in form.cleaned_data:
            if form.cleaned_data[field]:
                print(f"Filtering {field} with value {form.cleaned_data[field]}")
                queryset = queryset.filter(**{field+'__icontains': form.cleaned_data[field]})
    
    context = {
        "header": "List of Locations",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "list_location_master.html", context)

# Repeat similar updates for other views


@login_required
def add_location_master(request):
    return add_item(request, LocationMasterForm, 'Location has been added successfully', 'list_location_master')

@login_required
def update_location_master(request, pk):
    return update_item(request, pk, LocationMaster, LocationMasterForm, 'Location has been updated successfully', 'list_location_master')

@login_required
def delete_location_master(request, pk):
    return delete_item(request, pk, LocationMaster, 'list_location_master')

@login_required
def list_ssd(request):
    form = SSDSearchForm(request.GET or None)
    queryset = SSD.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        for field in form.cleaned_data:
            if form.cleaned_data[field]:
                queryset = queryset.filter({field+'__icontains': form.cleaned_data[field]})
    
    context = {
        "header": "List of SSDs",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "list_ssd.html", context)

@login_required
def add_ssd(request):
    return add_item(request, SSDForm, 'SSD has been added successfully', 'list_ssd')
@login_required
def update_ssd(request, pk):
    return update_item(request, pk, SSD, SSDForm, 'SSD has been updated successfully', 'list_ssd')

@login_required
def delete_ssd(request, pk):
    return delete_item(request, pk, SSD, 'list_ssd')

@login_required
def list_dtlt(request):
    header = "LIST OF DTLTs"
    form = DTLTSearchForm(request.GET or None)
    queryset = DTLT.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        serial_number = form.cleaned_data.get('serial_number')
        employee_id = form.cleaned_data.get('employee_id')
        
        if serial_number:
            queryset = queryset.filter(serial_number__icontains=serial_number)
        if employee_id:
            queryset = queryset.filter(employee_id__icontains=employee_id)
    
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    
    return render(request, "list_dtlt.html", context)



@login_required
def add_dtlt(request):
    return add_item(request, DTLTForm, 'DTLT has been added successfully', 'list_dtlt')
@login_required
def admin(request):
    return admin(request)

@login_required
def update_dtlt(request, pk):
    return update_item(request, pk, DTLT, DTLTForm, 'DTLT has been updated successfully', 'list_dtlt')

@login_required
def delete_dtlt(request, pk):
    return delete_item(request, pk, DTLT, 'list_dtlt')

@login_required
def list_dtltotnetwork(request):
    form = DTLTOTNetworkSearchForm(request.GET or None)
    queryset = DTLTOTNetwork.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        for field in form.cleaned_data:
            if form.cleaned_data[field]:
                queryset = queryset.filter(**{field+'__icontains': form.cleaned_data[field]})
    
    context = {
        "header": "List of OT Networks",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "list_dtltotnetwork.html", context)

@login_required
def add_dtltotnetwork(request):
    return add_item(request, DTLTOTNetworkForm, 'OT Network has been added successfully', 'list_dtltotnetwork')

@login_required
def update_dtltotnetwork(request, pk):
    return update_item(request, pk, DTLTOTNetwork, DTLTOTNetworkForm, 'OT Network has been updated successfully', 'list_dtltotnetwork')

@login_required
def delete_dtltotnetwork(request, pk):
    return delete_item(request, pk, DTLTOTNetwork, 'list_dtltotnetwork')

@login_required
def list_dtltretired(request):
    form = DTLTRetiredSearchForm(request.GET or None)
    queryset = DTLTRetired.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        for field in form.cleaned_data:
            if form.cleaned_data[field]:
                queryset = queryset.filter(**{field+'__icontains': form.cleaned_data[field]})
    
    context = {
        "header": "List of Retired DTLTs",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "list_dtltretired.html", context)

@login_required
def add_dtltretired(request):
    return add_item(request, DTLTRetiredForm, 'Retired DTLT has been added successfully', 'list_dtltretired')

@login_required
def update_dtltretired(request, pk):
    return update_item(request, pk, DTLTRetired, DTLTRetiredForm, 'Retired DTLT has been updated successfully', 'list_dtltretired')

@login_required
def delete_dtltretired(request, pk):
    return delete_item(request, pk, DTLTRetired, 'list_dtltretired')

@login_required
def list_printer(request):
    form = PrinterSearchForm(request.GET or None)
    queryset = Printer.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        for field in form.cleaned_data:
            if form.cleaned_data[field]:
                queryset = queryset.filter(**{field+'__icontains': form.cleaned_data[field]})
    
    context = {
        "header": "List of Printers",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "list_printer.html", context)

@login_required
def add_printer(request):
    return add_item(request, PrinterForm, 'Printer has been added successfully', 'list_printer')

@login_required
def update_printer(request, pk):
    return update_item(request, pk, Printer, PrinterForm, 'Printer has been updated successfully', 'list_printer')

@login_required
def delete_printer(request, pk):
    return delete_item(request, pk, Printer, 'list_printer')

@login_required
def list_vcprojectorstv(request):
    form = VCProjectorsTVSearchForm(request.GET or None)
    queryset = VCProjectorsTV.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        for field in form.cleaned_data:
            if form.cleaned_data[field]:
                queryset = queryset.filter(**{field+'__icontains': form.cleaned_data[field]})
    
    context = {
        "header": "List of VC Projectors and TVs",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "list_vcprojectorstv.html", context)

@login_required
def add_vcprojectorstv(request):
    return add_item(request, VCProjectorsTVForm, 'VC Projector/TV has been added successfully', 'list_vcprojectorstv')

@login_required
def update_vcprojectorstv(request, pk):
    return update_item(request, pk, VCProjectorsTV, VCProjectorsTVForm, 'VC Projector/TV has been updated successfully', 'list_vcprojectorstv')

@login_required
def delete_vcprojectorstv(request, pk):
    return delete_item(request, pk, VCProjectorsTV, 'list_vcprojectorstv')

@login_required
def list_ramdetails(request):
    form = RAMDetailsSearchForm(request.GET or None)
    queryset = RAMDetails.objects.all()
    
    if request.method == 'GET' and form.is_valid():
        for field in form.cleaned_data:
            if form.cleaned_data[field]:
                queryset = queryset.filter(**{field+'__icontains': form.cleaned_data[field]})
    
    context = {
        "header": "List of RAM Details",
        "queryset": queryset,
        "form": form,
    }
    return render(request, "list_ramdetails.html", context)

@login_required
def add_ramdetails(request):
    return add_item(request, RAMDetailsForm, 'RAM Detail has been added successfully', 'list_ramdetails')

@login_required
def update_ramdetails(request, pk):
    return update_item(request, pk, RAMDetails, RAMDetailsForm, 'RAM Detail has been updated successfully', 'list_ramdetails')

@login_required
def delete_ramdetails(request, pk):
    return delete_item(request, pk, RAMDetails, 'list_ramdetails')

def get_chart_data(request):
    # Check cache
    cached_data = cache.get("chart_data")
    if cached_data:
        return JsonResponse(cached_data)

    # Current date for warranty check
    current_date = timezone.now().date()

    # Aggregate Data
    assets = DTLT.objects.values('device_type').annotate(
        total_devices=Count('device_type'),
        to_operational=Count(Case(When(operational_status='Operational', then=1), output_field=IntegerField())),
        to_stock=Count(Case(When(operational_status='Stock', then=1), output_field=IntegerField())),
        to_retired=Count(Case(When(warranty_end_date__lt=current_date, then=1), output_field=IntegerField())),
        in_warranty=Count(Case(When(warranty_end_date__gte=current_date, then=1), output_field=IntegerField()))
    )

    # Prepare Data for Charts
    labels = []
    total_devices = []
    operational = []
    stock = []
    retired = []
    in_warranty = []

    for asset in assets:
        labels.append(asset['device_type'])
        total_devices.append(asset['total_devices'])
        operational.append(asset['to_operational'])
        stock.append(asset['to_stock'])
        retired.append(asset['to_retired'])
        in_warranty.append(asset['in_warranty'])

    # Format Data for Charts
    data = {
        "labels": labels,
        "pie_chart": {
            "labels": labels,
            "data": total_devices 
        },
        "bar_chart": {
            "labels": labels,
            "datasets": [
                {"label": "Operational", "data": operational, "backgroundColor": "#ff5733"},
                {"label": "Stock", "data": stock, "backgroundColor": "#ffbd33"},
                {"label": "Retired", "data": retired, "backgroundColor": "#75ff33"},
                {"label": "In Warranty", "data": in_warranty, "backgroundColor": "#27b6e8"},
            ]
        }
    }

    cache.set("chart_data", data, timeout=3000)
    return JsonResponse(data)

def dashboard(request):
    return render(request, 'dashboard.html')