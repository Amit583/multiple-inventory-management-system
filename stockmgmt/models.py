from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.utils import timezone  



# Location Master
class LocationMaster(models.Model):
    location_name = models.CharField(max_length=255)
    location_code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location_name

# SSD
class SSD(models.Model):
    serial_number = models.CharField(max_length=255, primary_key=True)
    model_name = models.CharField(max_length=255)
    capacity = models.IntegerField(help_text="Capacity in GB")
    manufacturer = models.CharField(max_length=255)
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
    asset_status = models.CharField(max_length=50, choices=[('active', 'Active'), ('retired', 'Retired')])
    created_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model_name} - {self.serial_number}"

# DTLT

class DTLT(models.Model):
    devicechoice = [('Desktop', 'Desktop'), ('Laptop', 'Laptop'), ('Workshop', 'Workshop')]
    device_type = models.CharField(max_length=100, choices=devicechoice,db_index=True)
    serial_number = models.CharField(max_length=100, unique=True)
    asset_owner_name = models.CharField(max_length=255)
    laptop_bag_issued_date = models.DateField(null=True, blank=True)
    manufacturer = models.CharField(max_length=255)
    model_description = models.TextField(blank=True, null=True)
    po_number = models.IntegerField()
    sap_code = models.CharField(max_length=255)
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField(null=True)
    asset_age = models.IntegerField(blank=True, null=True)
    asset_age_as_on = models.DateField(auto_now_add=True)
    asset_status = models.CharField(max_length=50,choices=[('Warranty', 'Warranty'), ('Expired', 'Expired')],blank=True)
    asset_tag = models.CharField(max_length=100, unique=True)
    host_name = models.CharField(max_length=100)
    operational_status = models.CharField(
        max_length=100,
        choices=[('Operational', 'Operational'), ('Stock', 'Stock')]
    )
    operational_remark = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    assigned_to_user = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.CharField(max_length=100, blank=True, null=True)
    user_dept = models.CharField(max_length=100, blank=True, null=True)
    user_location = models.CharField(max_length=255, blank=True, null=True)
    placement = models.CharField(max_length=255, blank=True, null=True)
    os_name = models.CharField(max_length=100)
    os_version = models.FloatField()
    office_version = models.CharField(max_length=100)
    CHOICESyes = [('yes', 'Yes'), ('no', 'No'), ('NA', 'NA')]
    Antivirus = models.CharField(max_length=50, choices=CHOICESyes)
    DLP = models.CharField(max_length=50, choices=CHOICESyes)
    pgpchoice = [('PGP', 'PGP'), ('Bitlocker', 'Bitlocker')]
    Encryption = models.CharField(max_length=50, choices=pgpchoice)
    bigfix = models.CharField(max_length=50, choices=CHOICESyes)
    ram_size = models.PositiveIntegerField(help_text="Size in GB")
    engchoice = [('Vivek Naik', 'Vivek Naik'), ('Ajay Rathod', 'Ajay Rathod')]
    engineer_name = models.CharField(max_length=255, choices=engchoice)
    remarks = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"DTLT - {self.serial_number} - {self.device_type}"



    def save(self, *args, **kwargs):
        # Use timezone.now() to get the current time in Asia/Kolkata timezone
        today = timezone.now().date()

        # Debugging: Check today's date and warranty_start_date
        print(f"Saving asset: {self.serial_number}")
        print(f"Today's Date: {today}")
        print(f"Warranty Start Date: {self.warranty_start_date}")

        # Calculate asset status based on warranty_end_date
        if self.warranty_end_date:
            if today <= self.warranty_end_date:
                self.asset_status = 'Warranty'
            else:
                self.asset_status = 'Expired'
        else:
            self.asset_status = 'Expired'

        # Calculate asset age based on warranty_start_date
        if self.warranty_start_date:
            # Calculate the asset age by comparing the current date with warranty_start_date
            self.asset_age = today.year - self.warranty_start_date.year

            # Adjust for incomplete years
            if today.month < self.warranty_start_date.month or (
                today.month == self.warranty_start_date.month and today.day < self.warranty_start_date.day):
                self.asset_age -= 1

            # Debugging: Print the calculated asset age
            print(f"Calculated Asset Age: {self.asset_age}")
        else:
            self.asset_age = 0
            print("No warranty_start_date set, asset_age defaulted to 0.")

        super().save(*args, **kwargs)


    def clean(self):
    # Validation for operational_status
        if self.operational_status == 'Operational':
            missing_fields = []
            if not self.assigned_to_user:
                missing_fields.append('assigned_to_user')
            if not self.employee_id:
                missing_fields.append('employee_id')
            if not self.user_dept:
                missing_fields.append('user_dept')
            if not self.user_location:
                missing_fields.append('user_location')
            if not self.placement:
                missing_fields.append('placement')
            if missing_fields:
                raise ValidationError(
                    f"The following fields are required when Operational Status is 'Operational': {', '.join(missing_fields)}"
                )
            super().clean()

    

        # Validation for Laptop Device Type
    def clean(self):
            if self.device_type == 'Laptop' and not self.laptop_bag_issued_date:
                raise ValidationError(
                    f"Laptop Issued Date is required when Device Type is 'Laptop'."
            )
            super().clean()

# DTLT_OT Network 
class DTLTOTNetwork(models.Model):
    network_name = models.CharField(max_length=255)
    network_id = models.CharField(max_length=50, unique=True)
    ip_range = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.network_name

# DTLT Retired
class DTLTRetired(models.Model):
    serial_number = models.CharField(max_length=255, primary_key=True)
    dtlt = models.CharField(max_length=255)
    retired_date = models.DateField()
    reason_for_retirement = models.CharField(max_length=255)
    retired_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Retired: {self.dtlt} - {self.serial_number}"

# Printer
class Printer(models.Model):
    serial_number = models.CharField(max_length=255, primary_key=True)
    model_name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
    asset_status = models.CharField(max_length=50, choices=[('active', 'Active'), ('retired', 'Retired')])
    created_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Printer - {self.model_name}"

# VC-projectors-TV
class VCProjectorsTV(models.Model):
    serial_number = models.CharField(max_length=255, primary_key=True)
    model_name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
    asset_status = models.CharField(max_length=50, choices=[('active', 'Active'), ('retired', 'Retired')])
    created_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"VC-Projector-TV - {self.model_name}"

# RAM Details
class RAMDetails(models.Model):
    ram_type = models.CharField(max_length=255)
    ram_size = models.IntegerField(help_text="Size in GB")
    serial_number = models.CharField(max_length=255, primary_key=True)
    manufacturer = models.CharField(max_length=255)
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
    asset_status = models.CharField(max_length=50, choices=[('active', 'Active'), ('retired', 'Retired')])
    created_by = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    vendordetail = models.CharField(max_length=255,blank=True,null=True)
    ponumber = models.CharField(max_length=255,blank=True,null=True)
    invoiceno = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return f"RAM - {self.ram_type} - {self.serial_number}"
