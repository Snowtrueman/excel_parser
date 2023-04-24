from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Data._meta.get_fields()]


admin.site.register(Data, DataAdmin)
