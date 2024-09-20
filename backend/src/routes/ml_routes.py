# backend/src/routes/ml_routes.py

from django.urls import path
from .controllers.ml_controller import MLModelView

urlpatterns = [
    path('train/', MLModelView.as_view(), name='train_ml_model'),
]
