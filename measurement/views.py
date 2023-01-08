from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer

class SensorCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'Ok'})

class OneSensorAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class MeasurementViewSet(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class ListSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

