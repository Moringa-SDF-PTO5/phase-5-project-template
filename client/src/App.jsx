
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CreateAccount from './register';
import { AppProvider } from './AppContext';
import OrderConfirmation from './OrderConfirmation';
import DeliveryConfirmation from './DeliveryConfirmation';
import Login from './login';
import HomePage from './HomePage';
import CategoryPage from './CategoryPage';
import OrderingPage from './OrderingPage';
import './App.css';

function App() {
    return (
        <Router>
            <AppProvider>
                <div className="app">
                    <Routes>
                        <Route path="/" element={<HomePage />} />
                        <Route path="/create-account" element={<CreateAccount />} />
                        <Route path="/login" element={<Login />} />
                        <Route path="/category/:categoryName" element={<CategoryPage />} />
                        <Route path="/confirmation" element={<OrderConfirmation />} />
                        <Route path="/delivery-confirmation" element={<DeliveryConfirmation />} />
                        <Route path="/ordering" element={<OrderingPage />} />
                    </Routes>
                </div>
            </AppProvider>
        </Router>
    );
}


export default App;

