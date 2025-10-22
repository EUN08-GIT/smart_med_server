from rest_framework import viewsets
from .models import User, Protector
from .serializers import UserSerializer, ProtectorSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ProtectorViewSet(viewsets.ModelViewSet):
    """
    보호자 CRUD API
    - 인증된 사용자만 접근 가능
    - Serializer를 통해 JSON 반환
    """
    queryset = Protector.objects.all() #모든 데이터(보호자데이터)를 조회
    serializer_class = ProtectorSerializer # 응답에 ProtectorSerializer로 json으로 변환해줌
    permission_classes = [IsAuthenticated] # 이건 인증된 사용자만 접근 가능
