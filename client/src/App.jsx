// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import OrderConfirmation from './OrderConfirmation';
import DeliveryConfirmation from './DeliveryConfirmation';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<OrderConfirmation />} />
          <Route path="/delivery-confirmation" element={<DeliveryConfirmation />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
