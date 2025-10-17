from rest_framework import serializers
from .models import Medication, MedicationSchedule, MedicationHistory

class MedicationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSchedule
        fields = ['id', 'scheduled_time']

class MedicationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationHistory
        fields = ['id', 'taken_time', 'status']

class MedicationSerializer(serializers.ModelSerializer):
    schedules = MedicationScheduleSerializer(many=True, read_only=True)
    histories = MedicationHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Medication
        fields = ['id', 'user', 'name', 'dose', 'times_per_day', 'intake_timing', 'start_date', 'end_date', 'schedules', 'histories']
