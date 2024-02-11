import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class StockAPI:
    BASE_URL = 'https://www.alphavantage.co/query'

    def __init__(self):
        self.api_key = settings.ALPHA_VANTAGE_API_KEY
        if not self.api_key:
            raise ImproperlyConfigured('Alpha Vantage API key is not configured in settings.py')

    def _make_request(self, params):
        """Utility method to make API requests and return JSON data."""
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_company_info(self, company_symbol):
        """Fetches company overview information."""
        params = {
            'function': 'OVERVIEW',
            'symbol': company_symbol,
            'apikey': self.api_key
        }
        return self._make_request(params)

    def get_analytics(self, company_symbol):
        """Fetches analytics for a given company symbol."""
        params = {
            'function': 'TIME_SERIES_DAILY',  # Adjusted to a valid function
            'symbol': company_symbol,
            'apikey': self.api_key
        }
        return self._make_request(params)
