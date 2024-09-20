

// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Dashboard from './pages/Dashboard';
import TrainModel from './pages/TrainModel';
import UnitySimulation from './pages/UnitySimulation';
import RealTimeData from './pages/RealTimeData';
import SendLog from './pages/SendLog';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/train-model" element={<TrainModel />} />
        <Route path="/unity-simulation" element={<UnitySimulation />} />
        <Route path="/real-time-data" element={<RealTimeData />} />
        <Route path="/send-log" element={<SendLog />} />
      </Routes>
    </Router>
  );
}

export default App;
