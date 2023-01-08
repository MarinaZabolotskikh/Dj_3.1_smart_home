from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Measurement)
class MeasurementAdnim(admin.ModelAdmin):
    pass

