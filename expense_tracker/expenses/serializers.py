from rest_framework import serializers
from .models import Category, Transaction

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category', 'created_at']


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'category', 'amount', 'description', 'date', 'created_at']
