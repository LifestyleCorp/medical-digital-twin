# backend/src/models/simulation_log.py

from djongo import models

class SimulationLog(models.Model):
    simulation_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    log_data = models.JSONField()

    class Meta:
        db_table = "simulation_log"
