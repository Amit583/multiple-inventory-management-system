from django import forms
from .models import (
    LocationMaster, SSD, DTLT, DTLTOTNetwork, DTLTRetired,
    Printer, VCProjectorsTV, RAMDetails
)

class LocationMasterForm(forms.ModelForm):
    class Meta:
        model = LocationMaster
        exclude = ['timestamp', 'last_updated']

class SSDForm(forms.ModelForm):
    class Meta:
        model = SSD
        exclude = ['timestamp', 'last_updated']
        widgets = {
            'warranty_start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'warranty_end_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }

class DTLTForm(forms.ModelForm):
    class Meta:
        model = DTLT
        exclude = ['timestamp', 'last_updated','asset_status','asset_as_age_on','asset_age']
        widgets = {
            'laptop_bag_issued_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'warranty_start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'warranty_end_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'asset_age_as_on': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'model_description': forms.TextInput(attrs={'class': 'form-control'}),
            'operational_remark': forms.TextInput(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
            'ram_size': forms.NumberInput(attrs={'placeholder': ' in GB'}),

        
        }

class DTLTOTNetworkForm(forms.ModelForm):
    class Meta:
        model = DTLTOTNetwork
        exclude = ['timestamp', 'last_updated']

class DTLTRetiredForm(forms.ModelForm):
    class Meta:
        model = DTLTRetired
        exclude = ['timestamp']
        widgets = {
            'retired_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        exclude = ['timestamp', 'last_updated']
        widgets = {
            'warranty_start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'warranty_end_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }

class VCProjectorsTVForm(forms.ModelForm):
    class Meta:
        model = VCProjectorsTV
        exclude = ['timestamp', 'last_updated']
        widgets = {
            'warranty_start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'warranty_end_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }

class RAMDetailsForm(forms.ModelForm):
    class Meta:
        model = RAMDetails
        exclude = ['timestamp', 'last_updated']
        widgets = {
            'warranty_start_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'warranty_end_date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }

# Adding Search Forms with placeholders
class LocationMasterSearchForm(forms.Form):
    location_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by location name'}))

class SSDSearchForm(forms.Form):
    serial_number = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by serial number'}))

class DTLTSearchForm(forms.Form):
    serial_number = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'serial number'}))
    employee_id = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'employee ID'}))

class DTLTOTNetworkSearchForm(forms.Form):
    network_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by network name'}))
    network_id = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by network ID'}))

class DTLTRetiredSearchForm(forms.Form):
    serial_number = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by serial number'}))

class PrinterSearchForm(forms.Form):
    serial_number = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by serial number'}))
    model_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by model name'}))

class VCProjectorsTVSearchForm(forms.Form):
    serial_number = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by serial number'}))
    model_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by model name'}))

class RAMDetailsSearchForm(forms.Form):
    serial_number = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by serial number'}))
    ram_type = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Search by RAM type'}))
