from rest_framework import viewsets, permissions
from .models import Company, DailyStockPrice
from .serializers import CompanySerializer, DailyStockPriceSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class DailyStockPriceViewSet(viewsets.ModelViewSet):
    queryset = DailyStockPrice.objects.all()
    serializer_class = DailyStockPriceSerializer
    permission_classes = [permissions.IsAuthenticated]
