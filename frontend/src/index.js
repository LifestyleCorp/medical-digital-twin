
import React from 'react';
import ReactDOM from 'react-dom/client';  // Import from react-dom/client for createRoot
import './index.css';
import App from './App';

// Create the root element for React 18
const root = ReactDOM.createRoot(document.getElementById('root'));

// Use root.render instead of ReactDOM.render
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

