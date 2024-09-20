# backend/src/routes/log_routes.py

from django.urls import path
from .controllers.log_controller import SimulationLogView

urlpatterns = [
    path('logs/', SimulationLogView.as_view(), name='simulation_logs'),
]
