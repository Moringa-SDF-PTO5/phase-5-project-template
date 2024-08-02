// src/DeliveryConfirmation.jsx
import React, { useEffect, useState } from 'react';
// import './DeliveryConfirmation.css';

const DeliveryConfirmation = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/products') 
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  return (
    <div className="delivery-confirmation">
      <h1>Delivery Confirmation</h1>
      <div className="products">
        {products.map(product => (
          <div key={product.id} className="product">
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>Price: ${product.price}</p>
          </div>
        ))}
      </div>
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

export default DeliveryConfirmation;
