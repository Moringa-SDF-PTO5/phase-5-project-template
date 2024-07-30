import React, { createContext, useState } from 'react';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false); 
  const [cartItems, setCartItems] = useState([]); 

  const login = () => setIsLoggedIn(true);
  const logout = () => setIsLoggedIn(false);
  const addToCart = (item) => {
    setCartItems((prevItems) => [...prevItems, item]);
  };

  const clearCart = () => setCartItems([]);

  return (
    <AppContext.Provider
      value={{ isLoggedIn, login, logout, cartItems, addToCart, clearCart }}
    >
      {children}
    </AppContext.Provider>
  );
};
