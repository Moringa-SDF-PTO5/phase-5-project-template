import React, { useContext, useState} from 'react';
import { useNavigate } from 'react-router-dom';
import { AppContext } from './AppContext';
import techlogo from './assets/techlogo.png';
import cart from './assets/cart.png';
import home from './assets/home.png';
import profile from './assets/profile.png';

const Navbar = () => {
  const { isLoggedIn, logout, cartItems } = useContext(AppContext);
  const [showCartDropdown, setShowCartDropdown] = useState(false);
  const [showProfileOptions, setShowProfileOptions] = useState(false);
  const navigate = useNavigate();

  const handleHomeClick = () => {
    navigate('/');
  };

  const handleCartClick = () => {
    if (isLoggedIn) {
      navigate('/ordering');
    } else {
      navigate('/login'); 
    }
  };

  const handleProfileClick = () => {
    setShowProfileOptions(!showProfileOptions);
  };

  const handleLogout = () => {
    logout();
    setShowProfileOptions(false);
  };

  return (
    <nav className="navbar">
        <div className='title'>
      <img src={techlogo} alt="Tech Haven Logo" className="logo" />
      <h1>TECH HAVEN</h1>
      </div>
      <div className="navbar-icons">
        <button className="icon-btn" onClick={handleHomeClick}>
          <img src={home} alt="Home" className="icon" />
        </button>
        <div
          className="icon-btn"
          onMouseEnter={() => setShowCartDropdown(true)}
          onMouseLeave={() => setShowCartDropdown(false)}
          onClick={handleCartClick}
        >
          <img src={cart} alt="Cart" className="icon" />
          {showCartDropdown && (
            <div className="cart-dropdown">
              {cartItems.length > 0 ? (
                cartItems.map((item) => (
                  <div key={item.id} className="cart-item">
                    <p>{item.name}</p>
                    <p>Qty: {item.quantity}</p>
                  </div>
                ))
              ) : (
                <p>No items in cart</p>
              )}
            </div>
          )}
        </div>
        <div className="icon-btn" onClick={handleProfileClick}>
          <img src={profile} alt="Profile" className="icon" />
          {showProfileOptions && (
            <div className="profile-options">
              {isLoggedIn ? (
                <>
                  <div className="option">Change Password</div>
                  <div className="option">My Orders</div>
                  <div className="option" onClick={handleLogout}>Log out</div>
                </>
              ) : (
                <div className="option" onClick={() => navigate('/login')}>Login</div>
              )}
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
