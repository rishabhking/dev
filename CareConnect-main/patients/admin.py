
from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'contact_number')
    search_fields = ('first_name', 'last_name', 'contact_number')

    def get_queryset(self, request):
        # Superusers can see all patients
        if request.user.is_superuser:
            return super().get_queryset(request)
        
        # Filter patients based on some custom user logic (adjust this as needed)
        # For example, we could filter based on a relationship between the user and patient,
        # such as if the logged-in user has an attribute linking them to specific patients.
        return super().get_queryset(request).filter(contact_number=request.user.username)

from django.contrib.auth.models import User

user = User.objects.get(username='CareConnect')
user.is_staff = True
user.save()
