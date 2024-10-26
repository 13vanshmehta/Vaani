// Footer.js
import React from 'react';
import { Mail , LampCeiling, MSquare} from 'lucide-react'; // Import social media icons

export const Footer = () => {
  return (
    <footer className="bg-black bg-opacity-90 text-gray-400 p-9 shadow-lg w-full">
      <div className="max-w-5xl mx-auto flex justify-between items-center">
        <div className="flex flex-col">
          <h4 className="font-bold text-white mb-2">Quick Links</h4>
          <ul>
            <li className="mb-1"><a href="#about" className="hover:text-white">About Us</a></li>
            <li className="mb-1"><a href="#services" className="hover:text-white">Services</a></li>
            <li className="mb-1"><a href="#contact" className="hover:text-white">Contact</a></li>
            <li><a href="#privacy" className="hover:text-white">Privacy Policy</a></li>
          </ul>
        </div>

        <div className="flex flex-col items-center">
          <h4 className="font-bold text-white mb-2">Follow Us</h4>
          <div className="flex space-x-4">
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
              <MSquare className="w-6 h-6 hover:text-white" />
            </a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
              <LampCeiling className="w-6 h-6 hover:text-white" />
            </a>
            <a href="mailto:info@example.com">
              <Mail className="w-6 h-6 hover:text-white" />
            </a>
          </div>
        </div>
      </div>

      <div className="text-center mt-4">
        <p>&copy; {new Date().getFullYear()} Anything. All rights reserved.</p>
      </div>
    </footer>
  );
};
