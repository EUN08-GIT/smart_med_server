
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime

from .serializers import SensorDataSerializer

def _normalize_item(item: dict) -> dict:
    # 키 매핑
    if 'sensorValue' in item and 'weight_change' not in item:
        item['weight_change'] = item.pop('sensorValue')
    if 'isOpened' in item and 'is_opened' not in item:
        item['is_opened'] = item.pop('isOpened')

    # 타입 보정
    def to_float(x):
        try: return float(x)
        except: return None

    def to_int(x):
        try: return int(x)
        except: return None

    def to_bool(x):
        if isinstance(x, bool): return x
        if isinstance(x, str): return x.strip().lower() in ("1","true","t","yes","y","on")
        return bool(x)

    # 예시 필드 보정 (모델 필드명에 맞게 조정)
    if 'weight_change' in item:
        item['weight_change'] = to_float(item['weight_change'])
    if 'heart_rate' in item:
        item['heart_rate'] = to_int(item['heart_rate'])
    if 'isOpened' in item:
        item['is_opened'] = to_bool(item['isOpened'])
    if 'timestamp' in item and isinstance(item['timestamp'], str):
        item['timestamp'] = parse_datetime(item['timestamp']) or item['timestamp']

    return item

@api_view(['POST'])
@permission_classes([AllowAny])
def receive_sensor_data(request):
    data = request.data
    if isinstance(data, dict):
        data = [data]

    results = []
    for item in data:
        item['is_opened'] = item.pop('isOpened', False)
        serializer = SensorDataSerializer(data=item)
        if serializer.is_valid():
            serializer.save()
            results.append({'status': 'ok'})
        else:
            results.append({'status': 'error', 'errors': serializer.errors})

    return Response(results)
