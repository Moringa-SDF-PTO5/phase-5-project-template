import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import techlogo from './assets/techlogo.png'

const Login = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        username: '',
        password: ''
    });
    const [error, setError] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const { username, password } = formData;

        try {
            const response = await fetch('http://localhost:5000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const user = await response.json();
                console.log(user); 
                navigate('/');
            } else {
                const result = await response.json();
                setError(result.message || 'An error occurred');
            }
        } catch (error) {
            setError('An error occurred. Please try again.');
        }
    };

    const handleSignUp = () => {
        navigate('/create-account');
    };

    return (
        <div className="login-container">
            <div className="header">
                <img src={techlogo} alt="Tech Haven Logo" className="logo" />
                <h1 className="title">TECH HAVEN</h1>
            </div>
            <div className="login-card">
                <h1 className="login-header">login</h1>
                {error && <p className="error">{error}</p>}
                <form className="login-form" onSubmit={handleSubmit}>
                    <label htmlFor="username">Username:</label>
                    <input
                        type="email"
                        id="username"
                        name="username"
                        placeholder="example@mail.com"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />

                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        placeholder="**********"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />

                    <button type="submit" className="login-button">Log in</button>
                </form>
                <p>Are you new here? <span onClick={handleSignUp} className="link">Click Here</span> to sign up</p>
            </div>
        </div>
    );
};

export default Login;
