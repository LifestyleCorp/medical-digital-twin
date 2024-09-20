# backend/src/routes/simulation_routes.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .controllers.simulation_controller import CellViewSet

router = DefaultRouter()
router.register(r'cells', CellViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
