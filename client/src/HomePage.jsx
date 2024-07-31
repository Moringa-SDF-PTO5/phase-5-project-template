import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from './NavBar';
import Footer from './footer';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import options from'./assets/options.png';

const HomePage = () => {
  const [categories, setCategories] = useState([]);
  const [carouselProducts, setCarouselProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    fetch('https://phase-5-project-group-2-server.onrender.com/products')
      .then(response => response.json())
      .then(data => {
        const categorizedProducts = data.reduce((acc, product) => {
          if (!acc[product.category_name]) {
            acc[product.category_name] = [];
          }
          acc[product.category_name].push(product);
          return acc;
        }, {});
        setCategories(Object.entries(categorizedProducts));
        setCarouselProducts(data.slice(0, 10)); 
      })
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredCategories = categories.map(([categoryName, products]) => {
    const filteredProducts = products.filter(product => 
      product.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    return [categoryName, filteredProducts];
  });

  const handleProductClick = (product) => {
    setSelectedProduct(product);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setSelectedProduct(null);
  };

  const handleViewAll = (categoryName) => {
    navigate(`/category/${categoryName}`);
  };

  return (
    <div>
      <Navbar />
      <div className="product-categories">
        <div className="search-bar">
          <input 
            type="text" 
            placeholder="Search..." 
            value={searchTerm}
            onChange={handleSearch} 
          />
          <img src={options} alt="options" className="options" />
        </div>
        <div className="carousel-wrapper">
          <Carousel showThumbs={false} autoPlay interval={3000} infiniteLoop>
            {carouselProducts.map(product => (
              <div key={product.product_id}>
                <img src={product.image} alt={product.name} />
                <p className="legend">{product.name}</p>
              </div>
            ))}
          </Carousel>
        </div>
        {filteredCategories.map(([categoryName, products], index) => (
          <div key={index} className="category">
            <h2>{categoryName}</h2>
            <div className="products">
              {products.slice(0, 8).map(product => (
                <div key={product.product_id} className="product" onClick={() => handleProductClick(product)}>
                  <div className="product-card">
                    <img src={product.image} alt={product.name} />
                    <p>{product.name}</p>
                  </div>
                </div>
              ))}
              <div className="view-all" onClick={() => handleViewAll(categoryName)}>
                <p>→ View All</p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <Footer />
      {showModal && selectedProduct && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>&times;</span>
            <img src={selectedProduct.image} alt={selectedProduct.name} />
            <h2>{selectedProduct.name}</h2>
            <p>{selectedProduct.description}</p>
            <p><strong>Price:</strong> Ksh {selectedProduct.price}</p>
            <p><strong>Stock Quantity:</strong> {selectedProduct.stock_quantity}</p>
            <p><strong>Category:</strong> {selectedProduct.category_name}</p>
            <button className="add-to-cart">Add to Cart</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default HomePage;
