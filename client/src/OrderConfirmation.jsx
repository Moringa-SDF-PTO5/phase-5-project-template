import React from 'react';
import { useNavigate } from 'react-router-dom';
import './OrderConfirmation.css';
import Navbar from './NavBar';
import Footer from './footer';

const OrderConfirmation = () => {
  const navigate = useNavigate();

  return (
    <div>
      <Navbar />
      <div className="order-confirmation">
        <h1>Your order is confirmed</h1>
        <p>Thank you for shopping with us</p>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8JHb5VnI5kadNpwvNGxOBSuCh__5cy8q3lQ&s"  />
        <p>Your order date will be sent to your email </p>
        <div className="confirmation-buttons">
          <button className="continue-shopping-button" onClick={() => navigate('/')}>Continue Shopping</button>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default OrderConfirmation;
