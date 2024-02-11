from django.test import TestCase
from django.utils import timezone

from portfolio.models import Company, DailyStockPrice


class CompanyModelTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.company = Company.objects.create(
            name="Test Company",
            industry="Finance",
            address="123 Test Lane",
            symbol="TC",
            sector="Banking",
        )

    def test_company_creation(self):
        """Test the company model can create a company."""
        self.assertIsInstance(self.company, Company)
        self.assertEqual(self.company.__str__(), "Test Company (TC)")

    def test_company_fields(self):
        """Test the fields of the company model."""
        self.assertEqual(self.company.name, "Test Company")
        self.assertEqual(self.company.industry, "Finance")
        self.assertEqual(self.company.address, "123 Test Lane")
        self.assertEqual(self.company.symbol, "TC")
        self.assertEqual(self.company.sector, "Banking")

class DailyStockPriceModelTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.company = Company.objects.create(
            name="Test Company",
            industry="Finance",
            symbol="TC",
        )
        self.stock_price = DailyStockPrice.objects.create(
            company=self.company,
            date=timezone.now().date(),
            open="100.00",
            close="150.00",
            high="200.00",
            low="50.00",
        )

    def test_daily_stock_price_creation(self):
        """Test the daily stock price model can create a stock price entry."""
        self.assertIsInstance(self.stock_price, DailyStockPrice)
        self.assertEqual(self.stock_price.__str__(), f"Test Company ({self.stock_price.date})")

    def test_daily_stock_price_fields(self):
        """Test the fields of the daily stock price model."""
        self.assertEqual(self.stock_price.company, self.company)
        self.assertEqual(self.stock_price.open, "100.00")
        self.assertEqual(self.stock_price.close, "150.00")
        self.assertEqual(self.stock_price.high, "200.00")
        self.assertEqual(self.stock_price.low, "50.00")
