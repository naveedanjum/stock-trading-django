import random
from datetime import timedelta
from django.utils import timezone
from faker import Faker
from .models import Company, DailyStockPrice

fake = Faker()

def generate_companies(number=10):
    for _ in range(number):
        name = fake.company()
        industry = fake.bs()
        address = fake.address()
        symbol = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
        sector = random.choice(['Technology', 'Finance', 'Healthcare', 'Consumer Goods', 'Utilities'])

        Company.objects.get_or_create(
            name=name,
            defaults={
                'industry': industry,
                'address': address.replace('\n', ', '),
                'symbol': symbol,
                'sector': sector,
            }
        )


def generate_stock_prices(days=30, for_all_companies=True):
    companies = Company.objects.all() if for_all_companies else Company.objects.order_by('?')[:5]

    for company in companies:
        for day in range(days):
            date = timezone.now().date() - timedelta(days=day)
            open_price = random.uniform(100, 500)
            close_price = open_price + random.uniform(-10, 10)
            high = max(open_price, close_price) + random.uniform(0, 10)
            low = min(open_price, close_price) - random.uniform(0, 10)
            DailyStockPrice.objects.get_or_create(
                company=company,
                date=date,
                defaults={
                    'open': open_price,
                    'close': close_price,
                    'high': high,
                    'low': low,
                }
            )


# # Generate fake companies
# generate_companies(number=10)
#
# # Generate fake daily stock prices for the last 30 days for all companies
# generate_stock_prices(days=30, for_all_companies=True)
