from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required    
def user_ehr_view(request):
    # Get the logged-in user's username and first name
    username = request.user.username
    first_name = request.user.first_name

    try:
        # Try to find the patient whose first name matches the username
        patient = Patient.objects.get(first_name=first_name)

        if patient.first_name == username:
            # If the match is found, render the EHR details page
            return render(request, 'patients/user_ehr_detail.html', {'patient': patient})
        else:
            # If no match is found, show an error message
            return HttpResponse("No matching EHR found.")
    
    except Patient.DoesNotExist:
        # If no patient record is found, show a message
        return HttpResponse("No matching EHR found in the database.")

# @login_required    
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    # Ensure only the patient (by matching username) or a staff member can access the record
    if request.user.first_name == patient.first_name and request.user.last_name == patient.last_name:
        return render(request, 'patients/patient_detail.html', {'patient': patient})
    else:
         return HttpResponse(f"Sorry, {request.user.first_name}, you are not authorized to view this record.")

def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')  # Redirect to patient list after deletion
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})
