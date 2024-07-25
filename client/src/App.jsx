import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CreateAccount from './register';
import Login from './login';

function App() {
    return (
        <Router>
            <div className="app">
                <Routes>
                    <Route path="/create-account" element={<CreateAccount />} />
                    <Route path="/login" element={<Login />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
