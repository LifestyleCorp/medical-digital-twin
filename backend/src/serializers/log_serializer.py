# backend/src/serializers/log_serializer.py

from rest_framework import serializers
from .models.simulation_log import SimulationLog

class SimulationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationLog
        fields = '__all__'
