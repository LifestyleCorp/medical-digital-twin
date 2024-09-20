# backend/src/cpp_module/binding.py

import ctypes
import os

# Load the shared library
lib_path = os.path.join(os.path.dirname(__file__), 'build', 'libsimulation.so')
simulation_lib = ctypes.CDLL(lib_path)

# Define the argument and return types
simulation_lib.performCalculation.argtypes = [ctypes.c_double]
simulation_lib.performCalculation.restype = ctypes.c_double

class Simulation:
    def __init__(self):
        pass

    def perform_calculation(self, input_value):
        return simulation_lib.performCalculation(input_value)
