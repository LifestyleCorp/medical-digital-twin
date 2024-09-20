# backend/src/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/simulation/', include('simulation.routes.simulation_routes')),
    path('api/ml/', include('simulation.routes.ml_routes')),
]

