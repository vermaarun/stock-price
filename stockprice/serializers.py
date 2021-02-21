from rest_framework import serializers
from .models import HistoricalData
from .models import CompanyList


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class for StockSerializer."""
        model = HistoricalData
        fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class for CompanyListSerializer."""
        model = CompanyList
        fields = '__all__'
