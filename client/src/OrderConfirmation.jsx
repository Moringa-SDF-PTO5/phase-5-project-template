
import React from 'react';
import './OrderConfirmation.css';

const OrderConfirmation = () => {
  return (
    <div className="order-confirmation">
      <h1>Thank You!</h1>
      <p>We are getting started on your order right away, and you will receive an order confirmation shortly via your email.</p>

      <div className="order-status">
        <h2>ORDER STATUS</h2>
        <p>Delivery pending</p>
      </div>

      <button className="view-order-button">VIEW ORDER CONFIRMATION</button>

      <footer className="footer">
        <div className="contact-info">
          <h3>Contact</h3>
          <p>+2547123456789</p>
        </div>

        <div className="address">
          <h3>Physical Address</h3>
          <p>Luthuli Street, Nairobi</p>
          <p>TECH HAVEN</p>
        </div>
      </footer>
    </div>
  );
};

export default OrderConfirmation;
