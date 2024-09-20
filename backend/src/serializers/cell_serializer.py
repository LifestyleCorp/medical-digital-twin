# backend/src/serializers/cell_serializer.py

from rest_framework import serializers
from .models.cell import Cell

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'
