# backend/src/controllers/simulation_controller.py

from rest_framework import viewsets
from .models.cell import Cell
from .serializers.cell_serializer import CellSerializer

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
