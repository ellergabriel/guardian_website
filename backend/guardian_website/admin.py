from django.contrib import admin
from .models import Guardian
# Register your models here.
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('fName', 'lName')

admin.site.register(Guardian, GuardianAdmin)