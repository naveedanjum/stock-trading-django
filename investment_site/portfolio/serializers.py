from rest_framework import serializers
from .models import Company, DailyStockPrice

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DailyStockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyStockPrice
        fields = '__all__'
