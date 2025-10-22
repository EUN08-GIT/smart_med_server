from django.contrib import admin
from django.urls import path, include
from users.urls import router as user_router
from medications.urls import router as med_router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(med_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/sensors/', include('sensors.urls')),
]
