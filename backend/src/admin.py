# backend/src/admin.py

from django.contrib import admin
from .models.simulation_log import SimulationLog

admin.site.register(SimulationLog)
