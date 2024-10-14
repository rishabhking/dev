# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin  # Import UserAdmin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from feedback.models import Feedback
from patients.models import Patient
class CustomAdminSite(admin.AdminSite):
    site_header = 'CareConnect Admin'
    site_title = 'CareConnect Admin Portal'
    index_title = 'Welcome to CareConnect Admin Portal'

# Instantiate the custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Register models with UserAdmin for password hashing
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group)
custom_admin_site.register(Permission)
custom_admin_site.register(ContentType)
custom_admin_site.register(Feedback)
custom_admin_site.register(Patient)
