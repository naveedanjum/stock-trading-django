from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from portfolio.models import Company, DailyStockPrice
from django.utils import timezone

class CompanyAPITests(APITestCase):

    def setUp(self):
        # Create a sample company
        self.company = Company.objects.create(
            name="Test Company",
            industry="Technology",
            address="123 Test Lane",
            symbol="TST",
            sector="Tech"
        )

    def test_get_companies(self):
        # Test retrieving a list of companies
        url = reverse('company-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.company.name)

    def test_get_company_detail(self):
        # Test retrieving a single company detail
        url = reverse('company-detail', args=[self.company.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.company.name)
