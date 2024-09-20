// frontend/src/pages/RealTimeData.js

import React, { useEffect, useState } from 'react';
import socket from '../services/socket';

const RealTimeData = () => {
  const [data, setData] = useState('');

  useEffect(() => {
    socket.on('receiveData', (newData) => {
      setData(newData);
    });

    return () => {
      socket.off('receiveData');
    };
  }, []);

  const sendData = () => {
    socket.emit('sendData', 'Hello from frontend!');
  };

  return (
    <div>
      <h2>Real-Time Data</h2>
      <button onClick={sendData}>Send Data</button>
      <p>Received: {data}</p>
    </div>
  );
};

export default RealTimeData;
