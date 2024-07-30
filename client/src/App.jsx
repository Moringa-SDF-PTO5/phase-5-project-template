import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CreateAccount from './register';
import { AppProvider } from './AppContext';
import Login from './login';
import HomePage from './HomePage';
import CategoryPage from './CategoryPage';

function App() {
    return (
        <AppProvider>
        <Router>
            <div className="app">
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/create-account" element={<CreateAccount />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/category/:categoryName" element={<CategoryPage />} />
                </Routes>
            </div>
        </Router>
        </AppProvider>
    );
}

export default App;
