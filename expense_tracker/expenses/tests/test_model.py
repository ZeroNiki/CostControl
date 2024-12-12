from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from expenses.models import Category, Transaction


class CategoryModelTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )

        self.category = Category.objects.create(name="Transport", user=self.user)

    def test_category_str(self):
        self.assertEqual(str(self.category), "Transport")


class TransactionModelTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )

        self.category = Category.objects.create(name="Transport", user=self.user)

        self.transaction = Transaction.objects.create(
            category=self.category,
            amount=-50,
            description="Taxi ride",
            date=timezone.now().isoformat(),
            user=self.user,
        )

    def test_transaction_str(self):
        self.assertEqual(str(self.transaction.category), str(self.category.name))
        self.assertEqual(self.transaction.amount, -50)
        self.assertEqual(str(self.transaction.description), "Taxi ride")
