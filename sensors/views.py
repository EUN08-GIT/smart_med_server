from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SensorDataSerializer


@api_view(['POST'])
def receive_sensor_data(request):
    data = request.data

    # 단일 객체 처리
    if isinstance(data, dict):
        data = [data]

    if isinstance(data, list):
        results = []
        for item in data:
#           item["weight_change"] = item.pop('sensorValue', None)
            item['is_opened'] = item.pop('isOpened', False)
#            item['heart_rate'] = item.get('heart_rate', 0)

            serializer = SensorDataSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                results.append({'status': 'ok', 'data': serializer.data})
            else:
                results.append({'status': 'error', 'errors': serializer.errors})
        return Response(results)



    return Response({"status": "error", "message": "Invalid data format"}, status=400)


