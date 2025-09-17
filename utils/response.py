from rest_framework.response import Response
from utils.datetime_helper import get_current_datetime

def api_response(message="Request successful", data=None, http_status=200):
    curr_datetime = get_current_datetime()
    return Response({
        'success': True,
        'statusCode': http_status,
        'message': message,
        'data': data,
        'timestamp': curr_datetime 
    }, status=http_status)