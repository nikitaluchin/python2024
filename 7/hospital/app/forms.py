from django.forms import ModelForm

from app.models import Patient

class CreatePatientModelForm(ModelForm):
    # validation should be here...

    class Meta:
        model = Patient
        fields = '__all__'
