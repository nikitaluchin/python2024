from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/create/', views.PatientCreate.as_view(template_name="app/patient_form.html"), name='patient-create'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(template_name="app/patient_detail.html"), name='patient-detail'),
    path('person/<int:pk>', views.PersonDetailView.as_view(template_name="app/person_detail.html"), name='person-detail'),
]
