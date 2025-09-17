from utils.response import api_response
from rest_framework.views import APIView

class AuthLoginViews(APIView):
    def get(self, request):
        tokens = {
            'access_token': 'alsdjfalsfja', 
            'refresh_token': 'asldjf;alsdfj'
        }
        return api_response(
            message='Login success',
            data=tokens,
            http_status=200
        )