from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet, DailyStockPriceViewSet
from .views import stock_graph
from .views import DailyStockPriceList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'daily-stock-prices', DailyStockPriceViewSet)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('stock-graph', stock_graph, name='stock_graph'),
    path('', include(router.urls)),
    path('stocks/<str:symbol>/', DailyStockPriceList.as_view(), name='daily-stock-prices'),
]
