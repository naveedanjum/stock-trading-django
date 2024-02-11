from django.core.management.base import BaseCommand
from portfolio.utils import generate_companies, generate_stock_prices


class Command(BaseCommand):
    help = 'Generates fake data for companies and daily stock prices'

    def add_arguments(self, parser):
        parser.add_argument('--companies', type=int, help='Number of companies to generate')
        parser.add_argument('--days', type=int, help='Number of days of stock prices to generate')

    def handle(self, *args, **options):
        companies = options['companies'] or 10  # Default to generating data for 10 companies
        days = options['days'] or 30  # Default to generating data for the past 30 days

        generate_companies(number=companies)
        generate_stock_prices(days=days, for_all_companies=True)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully generated {companies} companies and {days} days of stock prices.'))
