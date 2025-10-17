from rest_framework import viewsets
from .models import User, Protector
from .serializers import UserSerializer, ProtectorSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ProtectorViewSet(viewsets.ModelViewSet):
    queryset = Protector.objects.all()
    serializer_class = ProtectorSerializer
    permission_classes = [IsAuthenticated]
