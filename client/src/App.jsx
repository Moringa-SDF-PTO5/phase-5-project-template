import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CreateAccount from './register';
import OrderConfirmation from './OrderConfirmation';
import Login from './login';
import './App.css';

function App() {
    return (
        <Router>
            <div className="app">
                <Routes>
                    <Route path="/create-account" element={<CreateAccount />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/order-confirmation" element={<OrderConfirmation />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
