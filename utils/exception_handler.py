from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from utils.datetime_helper import get_current_datetime

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    curr_datetime = get_current_datetime()
    if response is not None:
        response.data = {
            'success': False,
            'statusCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': 'Internal Server Error',
            'data': response.get('details', 'An error occurred'),
            'timestamp': curr_datetime 
        }   
    else:
        response = Response({
            'success': False,
            'statusCode': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': str(exc),
            'data': None,
            'timestamp': curr_datetime 
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response