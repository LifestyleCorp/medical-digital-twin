# backend/src/controllers/ml_controller.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from ml_models.tensorflow_model import create_tf_model, train_tf_model
from ml_models.pytorch_model import PyTorchModel, train_pytorch_model
import torch

class MLModelView(APIView):
    def post(self, request, format=None):
        data = request.data.get('data')
        model_type = request.data.get('model_type', 'tensorflow')

        if not data:
            return Response({"error": "No data provided."}, status=status.HTTP_400_BAD_REQUEST)

        X = np.array(data['X'])
        y = np.array(data['y'])

        if model_type == 'tensorflow':
            model = create_tf_model(input_dim=X.shape[1], output_dim=y.shape[1])
            model = train_tf_model(model, X, y, epochs=20)
            # Save the model
            model.save('ml_models/tf_model.h5')
            return Response({"message": "TensorFlow model trained and saved."}, status=status.HTTP_200_OK)

        elif model_type == 'pytorch':
            model = PyTorchModel(input_dim=X.shape[1], output_dim=y.shape[1])
            X_tensor = torch.tensor(X, dtype=torch.float32)
            y_tensor = torch.tensor(y, dtype=torch.float32)
            model = train_pytorch_model(model, X_tensor, y_tensor, epochs=20)
            # Save the model
            torch.save(model.state_dict(), 'ml_models/pytorch_model.pth')
            return Response({"message": "PyTorch model trained and saved."}, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Invalid model type specified."}, status=status.HTTP_400_BAD_REQUEST)
