// frontend/src/pages/Dashboard.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [cells, setCells] = useState([]);

  useEffect(() => {
    fetchCells();
  }, []);

  const fetchCells = async () => {
    try {
      const response = await axios.get('/api/simulation/cells/');
      setCells(response.data);
    } catch (error) {
      console.error('Error fetching cells:', error);
    }
  };

  return (
    <div>
      <h2>Cellular Data</h2>
      <ul>
        {cells.map(cell => (
          <li key={cell.id}>{cell.name}: {cell.function}</li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
