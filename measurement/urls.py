from django.urls import path
from .views import SensorCreateAPIView, OneSensorAPIView, MeasurementViewSet, ListSensors

urlpatterns = [
    path('sensors/create/', SensorCreateAPIView.as_view()),
    path('sensor/<pk>/', OneSensorAPIView.as_view()),
    path('measurements/', MeasurementViewSet.as_view()),
    path('list/', ListSensors.as_view()),
]
