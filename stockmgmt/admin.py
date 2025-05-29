from django.contrib import admin
from django.contrib.auth.models import User  # Import User model for customization
from .forms import (
    LocationMasterForm, SSDForm, DTLTForm, DTLTOTNetworkForm, DTLTRetiredForm,
    PrinterForm, VCProjectorsTVForm, RAMDetailsForm
)
from .models import (
    LocationMaster, SSD, DTLT, DTLTOTNetwork, DTLTRetired,
    Printer, VCProjectorsTV, RAMDetails
)

# Base Admin Class for Adding Media (JS and CSS)
class CustomAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',  # jQuery
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',  # jQuery UI
        )
        css = {
            'all': ('https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',)
        }

# # Custom User Admin for Change User Page
# class CustomUserAdmin(admin.ModelAdmin):
#     change_form_template = 'admin/auth/user/change_form.html'  # Custom template for Change User
#   # list_display = ['id_password']  # Fields to display
#   # search_fields = ['username', 'email', 'first_name', 'last_name']  # Enable search

# # Unregister Default User Model and Register with Custom Admin
# admin.site.unregister(User)  # Unregister the default User admin
# admin.site.register(User, CustomUserAdmin)  # Register with CustomUserAdmin


from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms

class CustomUserAdmin(UserAdmin):
    # fieldsets
    fieldsets = (
        ('', {'fields': ('username', 'password')}),
        ('', {'fields': ('first_name', 'last_name', 'email')}),
        ('', {'fields': ('groups',)}), 
        ('', {'fields': ('user_permissions',)}),
        ('', {'fields': ('last_login', 'date_joined')}),
    )




# Admin Classes for Other Models
class LocationMasterAdmin(CustomAdmin):
    form = LocationMasterForm
    list_display = ['location_name', 'location_code', 'description', 'timestamp', 'last_updated']
    search_fields = ['location_name', 'location_code']

class SSDAdmin(CustomAdmin):
    form = SSDForm
    list_display = ['serial_number', 'model_name', 'capacity', 'manufacturer', 'warranty_start_date',
                    'warranty_end_date', 'asset_status', 'created_by', 'timestamp', 'last_updated']
    search_fields = ['serial_number', 'model_name']

class DTLTAdmin(CustomAdmin):
    form = DTLTForm
    list_display = ['device_type', 'serial_number', 'asset_owner_name', 'manufacturer',
                    'warranty_start_date', 'warranty_end_date', 'asset_status', 'host_name',
                    'assigned_to_user', 'timestamp']
    search_fields = ['serial_number', 'asset_owner_name', 'device_type']

class DTLTOTNetworkAdmin(CustomAdmin):
    form = DTLTOTNetworkForm
    list_display = ['network_name', 'network_id', 'ip_range', 'created_by', 'timestamp', 'last_updated']
    search_fields = ['network_name', 'network_id']

class DTLTRetiredAdmin(CustomAdmin):
    form = DTLTRetiredForm
    list_display = ['serial_number', 'dtlt', 'retired_date', 'reason_for_retirement',
                    'retired_by', 'timestamp']
    search_fields = ['serial_number', 'dtlt']

class PrinterAdmin(CustomAdmin):
    form = PrinterForm
    list_display = ['serial_number', 'model_name', 'manufacturer', 'warranty_start_date',
                    'warranty_end_date', 'asset_status', 'created_by', 'timestamp', 'last_updated']
    search_fields = ['serial_number', 'model_name']

class VCProjectorsTVAdmin(CustomAdmin):
    form = VCProjectorsTVForm
    list_display = ['serial_number', 'model_name', 'manufacturer', 'warranty_start_date',
                    'warranty_end_date', 'asset_status', 'created_by', 'timestamp', 'last_updated']
    search_fields = ['serial_number', 'model_name']

class RAMDetailsAdmin(CustomAdmin):
    form = RAMDetailsForm
    list_display = ['serial_number', 'ram_type', 'ram_size', 'manufacturer', 'warranty_start_date',
                    'warranty_end_date', 'asset_status', 'created_by', 'timestamp', 'last_updated']
    search_fields = ['serial_number', 'ram_type']

# Registered models with the custom admin classes
admin.site.register(LocationMaster, LocationMasterAdmin)
admin.site.register(SSD, SSDAdmin)
admin.site.register(DTLT, DTLTAdmin)
admin.site.register(DTLTOTNetwork, DTLTOTNetworkAdmin)
admin.site.register(DTLTRetired, DTLTRetiredAdmin)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(VCProjectorsTV, VCProjectorsTVAdmin)
admin.site.register(RAMDetails, RAMDetailsAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
