# backend/tests/test_models.py

import pytest
from src.models.cell import Cell

@pytest.mark.django_db
def test_create_cell():
    cell = Cell.objects.create(name="Neuron", function="Signal transmission")
    assert cell.name == "Neuron"
    assert cell.function == "Signal transmission"
    assert cell.id is not None
