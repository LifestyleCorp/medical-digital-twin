# backend/src/controllers/simulation_controller.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models.cell import Cell
from .serializers.cell_serializer import CellSerializer
from cpp_module.binding import Simulation

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cell = serializer.save()

        # Perform C++ calculation
        simulation = Simulation()
        result = simulation.perform_calculation(cell.id)
        
        return Response({"cell": serializer.data, "calculation_result": result}, status=status.HTTP_201_CREATED)


# backend/src/controllers/simulation_controller.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models.cell import Cell
from .serializers.cell_serializer import CellSerializer
from services.copasi_service import run_copasi_simulation

class SimulationViewSet(viewsets.ViewSet):
    def simulate(self, request):
        copasi_file = request.FILES.get('copasi_file')
        if not copasi_file:
            return Response({"error": "No COPASI file provided."}, status=status.HTTP_400_BAD_REQUEST)

        copasi_file_path = os.path.join('/tmp', copasi_file.name)
        output_file_path = os.path.join('/tmp', 'simulation_output.txt')

        with open(copasi_file_path, 'wb') as f:
            f.write(copasi_file.read())

        results = run_copasi_simulation(copasi_file_path, output_file_path)

        return Response({"results": results}, status=status.HTTP_200_OK)
