from django.db import models
from django.urls import reverse

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house_number = models.IntegerField()

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    contact_number = models.IntegerField()
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}, {self.middle_name}, {self.surname}"

class StaffType(models.Model):
    staff_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.type_name}"

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_type = models.ForeignKey(StaffType, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"staff id: {self.staff_id}, staff type id: {self.staff_type_id}, person: {self.person}"

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    supervised_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    room = models.IntegerField()
    age = models.IntegerField()
    diagnosis = models.CharField(max_length=100)

    def __str__(self):
        return f"patient id: {self.patient_id} diagnosis: {self.diagnosis}"

    def get_absolute_url(self):
        return reverse("patient-detail", kwargs={"pk": self.pk})