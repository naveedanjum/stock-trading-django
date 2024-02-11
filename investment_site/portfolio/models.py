from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    symbol = models.CharField(max_length=255, unique=True)
    sector = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'companies'
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
        ]

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class DailyStockPrice(models.Model):
    company = models.ForeignKey(Company, related_name='daily_prices', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'daily_stock_prices'
        unique_together = ('company', 'date')
        indexes = [
            models.Index(fields=['date'], name='date_idx'),
        ]

    def __str__(self):
        return f"{self.company.name} ({self.date})"