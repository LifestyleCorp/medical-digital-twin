// frontend/src/pages/TrainModel.js

import React, { useState } from 'react';
import axios from 'axios';

const TrainModel = () => {
  const [modelType, setModelType] = useState('tensorflow');
  const [X, setX] = useState('');
  const [y, setY] = useState('');
  const [message, setMessage] = useState('');

  const handleTrain = async () => {
    const data = {
      model_type: modelType,
      data: {
        X: JSON.parse(X),
        y: JSON.parse(y),
      },
    };

    try {
      const response = await axios.post('/api/ml/train/', data);
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Training failed.');
    }
  };

  return (
    <div>
      <h2>Train Machine Learning Model</h2>
      <label>
        Model Type:
        <select value={modelType} onChange={(e) => setModelType(e.target.value)}>
          <option value="tensorflow">TensorFlow</option>
          <option value="pytorch">PyTorch</option>
        </select>
      </label>
      <br />
      <label>
        Training Data X (JSON Array):
        <textarea value={X} onChange={(e) => setX(e.target.value)} />
      </label>
      <br />
      <label>
        Training Data y (JSON Array):
        <textarea value={y} onChange={(e) => setY(e.target.value)} />
      </label>
      <br />
      <button onClick={handleTrain}>Train Model</button>
      <p>{message}</p>
    </div>
  );
};

export default TrainModel;
