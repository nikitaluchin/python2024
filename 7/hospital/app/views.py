from django.shortcuts import render
from .models import Patient

def index(request):
    """View function for home page of site."""

    num_patients = Patient.objects.count()
    patients = Patient.objects.all()

    context = {
        'num_patients': num_patients,
        'patients': patients,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
