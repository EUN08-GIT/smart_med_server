from rest_framework import viewsets
from .models import Medication, MedicationSchedule, MedicationHistory
from .serializers import MedicationSerializer, MedicationScheduleSerializer, MedicationHistorySerializer
from rest_framework.permissions import IsAuthenticated

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]

class MedicationScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicationSchedule.objects.all()
    serializer_class = MedicationScheduleSerializer
    permission_classes = [IsAuthenticated]

class MedicationHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicationHistory.objects.all()
    serializer_class = MedicationHistorySerializer
    permission_classes = [IsAuthenticated]
