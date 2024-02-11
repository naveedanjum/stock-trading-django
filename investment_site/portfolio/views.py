from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Company, DailyStockPrice
from .serializers import CompanySerializer, DailyStockPriceSerializer
from django.shortcuts import render
from rest_framework import generics
from datetime import timedelta
from django.utils import timezone

class DailyStockPriceList(generics.ListAPIView):
    serializer_class = DailyStockPriceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given company,
        by filtering against a `symbol` query parameter in the URL.
        """
        queryset = DailyStockPrice.objects.all()
        symbol = self.kwargs['symbol']  # Assuming you're capturing 'symbol' from the URL
        today = timezone.now().date()
        thirty_days_ago = today - timedelta(days=30)

        company = Company.objects.filter(symbol=symbol).first()
        if company:
            queryset = queryset.filter(company=company, date__range=[thirty_days_ago, today])
        return queryset

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class DailyStockPriceViewSet(viewsets.ModelViewSet):
    queryset = DailyStockPrice.objects.all()
    serializer_class = DailyStockPriceSerializer
    permission_classes = [permissions.IsAuthenticated]


def stock_graph(request):
    return render(request, 'stock_price.html')
