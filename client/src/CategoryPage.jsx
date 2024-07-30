import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const CategoryPage = () => {
  const { categoryName } = useParams();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch the products from the server
    fetch('https://phase-5-project-group-2-server.onrender.com/products')
      .then(response => response.json())
      .then(data => {
        // Filter products based on the categoryName parameter
        const filteredProducts = data.filter(product => product.category_name === categoryName);
        setProducts(filteredProducts);
      })
      .catch(error => console.error('Error fetching products:', error));
  }, [categoryName]);

  return (
    <div>
      <h1>{categoryName}</h1>
      <div className="products">
        {products.map(product => (
          <div key={product.product_id} className="product-card">
            <img src={product.image} alt={product.name} />
            <p>{product.name}</p>
            <p>Ksh {product.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CategoryPage;
