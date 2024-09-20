

// frontend/src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <h1>Human Digital Twin Project</h1>
      <nav>
        <ul>
          <li><Link to="/">Dashboard</Link></li>
          <li><Link to="/train-model">Train Model</Link></li>
          <li><Link to="/unity-simulation">Unity Simulation</Link></li>
          <li><Link to="/real-time-data">Real-Time Data</Link></li>
          <li><Link to="/send-log">Send Log</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
