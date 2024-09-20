# backend/src/services/copasi_service.py

import subprocess
import os

def run_copasi_simulation(copasi_file_path, output_file_path):
    try:
        subprocess.run(['copasi-cli', '-c', 'Simulate', '-i', copasi_file_path, '-o', output_file_path], check=True)
        with open(output_file_path, 'r') as f:
            results = f.read()
        return results
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
