from utils.response import api_response
from rest_framework.views import APIView
from utils.third_party_apis import nse_ind_api
from apps.stocks.services.stock_service import StockService

class Top4Indices(APIView):
    def get(self, request):
        data = StockService.get_top_4_indices()
        return api_response(data=data)
    
class TopGainersLosers(APIView):
    def get(self, request):
        data = StockService.top_gainers_losers()
        return api_response(data=data)
    
class PopularStocks(APIView):
    def get(self, request):
        data = StockService.get_popular_stocks()
        return api_response(data=data)
    
class SearchStock(APIView):
    def get(self, request):
        data = StockService.search_stocks(request)
        return api_response(data=data) 
    
class GetStock(APIView):
    def get(self, request, symbol):
        data = StockService.get_stock_by_symbol(symbol)
        return api_response(data=data)
    