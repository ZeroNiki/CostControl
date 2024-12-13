from django.contrib.auth import get_user_model
from django.utils import timezone
from expenses.models import Category
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class CategoryAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass",
        )

        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def test_create_category(self):
        url = "http://127.0.0.1:8000/api/categories/"
        data = {"name": "Transport"}
        response = self.client.post(
            url, data, HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Transport")


class TransactionAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass",
        )
        self.category = Category.objects.create(
            name="Transport", user=self.user
        )

        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def test_create_transaction(self):
        url = "http://127.0.0.1:8000/api/transactions/"
        data = {
            "category": self.category.id,
            "amount": "-50.00",
            "description": "Taxi ride",
            "date": timezone.now().isoformat(),
        }
        response = self.client.post(
            url, data, HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["category"], self.category.id)
        self.assertEqual(str(response.data["amount"]), str(data["amount"]))
        self.assertEqual(response.data["description"], data["description"])
