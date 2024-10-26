import React from 'react';
import "./header.css"
import { NavLink } from 'react-router-dom';

export const Header = () => {
  return (
    <header className="fixed top-0 left-0 w-full bg-transparent p-4 z-[9999]">
      <nav className="max-w-7xl mx-auto background-clr rounded-xl shadow-lg">
        <div className="px-6 py-3 flex items-center justify-between">
          <div className="text-white font-semibold text-xl">
            <NavLink to ="/" >LOGO</NavLink>
          </div>

          <div className="flex items-center gap-4">
            <button className="px-4 py-2 text-gray-300 hover:text-white transition-colors">
              <NavLink to="/contact-us">Contact-Us</NavLink>
            </button>
            <button className="px-4 py-2 bg-white hover:bg-gray-100 text-gray-900 rounded-lg transition-colors">
              <NavLink to="/login">Sign-In</NavLink>
            </button>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;