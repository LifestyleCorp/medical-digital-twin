// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Dashboard from './pages/Dashboard';
import TrainModel from './pages/TrainModel';
import UnitySimulation from './pages/UnitySimulation';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/train-model" element={<TrainModel />} />
        <Route path="/unity-simulation" element={<UnitySimulation />} />
      </Routes>
    </Router>
  );
}

export default App;
