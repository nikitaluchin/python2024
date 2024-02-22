from django.contrib import admin
from .models import Address, Person, StaffType, Staff, Patient

# admin.site.register(Address)
# admin.site.register(Person)
# admin.site.register(StaffType)
# admin.site.register(Staff)
# admin.site.register(Patient)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number')
    list_filter = ('city',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'surname', 'contact_number', 'date_of_birth', 'sex', 'address_id')
    list_filter = ('date_of_birth', 'sex')

@admin.register(StaffType)
class StaffTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_type_id', 'person_id')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('person_id', 'supervised_by_id', 'room', 'age', 'diagnosis')
    list_filter = ('age',)
