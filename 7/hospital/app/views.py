from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Patient, Person


def index(request):
    """View function for home page of site."""

    num_patients = Patient.objects.count()
    patients = Patient.objects.all()

    context = {
        'num_patients': num_patients,
        'patients': patients,
    }

    return render(request, 'index.html', context=context)

class PersonDetailView(DetailView):
    model = Person
    fields = '__all__'

class PatientDetailView(DetailView):
    model = Patient
    fields = '__all__'

class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
