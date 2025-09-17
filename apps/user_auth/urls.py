from django.urls import path
from .views.auth_views import AuthLoginViews

urlpatterns = [
    path('login/', AuthLoginViews.as_view()),
]
