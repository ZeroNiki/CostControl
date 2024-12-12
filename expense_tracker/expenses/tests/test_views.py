from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken


class CategoryViewSetTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )

        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def test_category_list_view(self):
        response = self.client.get(
            "http://127.0.0.1:8000/api/categories/",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)


class TransactionViewSetTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )

        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def test_transaction_list_view(self):
        response = self.client.get(
            "http://127.0.0.1:8000/api/transactions/",
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)
