from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, DailyStockPriceViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'daily-stock-prices', DailyStockPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
