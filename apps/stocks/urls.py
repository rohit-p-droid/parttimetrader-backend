from django.urls import path
from .views.stock_views import Top4Indices, TopGainersLosers, PopularStocks, SearchStock, GetStock

urlpatterns = [
    path('top-4-indices', Top4Indices.as_view()),
    path('top-losers-gainers', TopGainersLosers.as_view()),
    path('popular-stocks', PopularStocks.as_view()),
    path('search', SearchStock.as_view()),
    path('search/<str:symbol>', GetStock.as_view()),
]
