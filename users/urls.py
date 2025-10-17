from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProtectorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'protectors', ProtectorViewSet)
