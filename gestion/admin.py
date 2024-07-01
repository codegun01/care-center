from django.contrib import admin
from .models import Patients

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Patients, PatientAdmin)