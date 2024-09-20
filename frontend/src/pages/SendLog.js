// frontend/src/pages/SendLog.js

import React, { useState } from 'react';
import axios from 'axios';

const SendLog = () => {
  const [simulationId, setSimulationId] = useState('');
  const [logData, setLogData] = useState('');
  const [message, setMessage] = useState('');

  const handleSendLog = async () => {
    const data = {
      simulation_id: simulationId,
      log_data: JSON.parse(logData),
    };

    try {
      const response = await axios.post('/api/logs/', data);
      setMessage('Log sent successfully.');
    } catch (error) {
      setMessage('Failed to send log.');
    }
  };

  return (
    <div>
      <h2>Send Simulation Log</h2>
      <label>
        Simulation ID:
        <input
          type="text"
          value={simulationId}
          onChange={(e) => setSimulationId(e.target.value)}
        />
      </label>
      <br />
      <label>
        Log Data (JSON):
        <textarea
          value={logData}
          onChange={(e) => setLogData(e.target.value)}
        />
      </label>
      <br />
      <button onClick={handleSendLog}>Send Log</button>
      <p>{message}</p>
    </div>
  );
};

export default SendLog;
