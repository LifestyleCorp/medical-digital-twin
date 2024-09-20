# backend/src/controllers/log_controller.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.simulation_log import SimulationLog
from .serializers.log_serializer import SimulationLogSerializer

class SimulationLogView(APIView):
    def post(self, request, format=None):
        serializer = SimulationLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
