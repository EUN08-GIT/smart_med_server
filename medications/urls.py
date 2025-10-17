from rest_framework.routers import DefaultRouter
from .views import MedicationViewSet, MedicationScheduleViewSet, MedicationHistoryViewSet

router = DefaultRouter()
router.register(r'medications', MedicationViewSet)
router.register(r'schedules', MedicationScheduleViewSet)
router.register(r'histories', MedicationHistoryViewSet)
