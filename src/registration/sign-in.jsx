import React from 'react';
import { NavLink } from 'react-router-dom';

export const Signin = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-web p-6">
      <div className="flex w-full max-w-4xl rounded-lg overflow-hidden shadow-lg">
        {/* 3D Abstract/Image Div */}
        <div className="w-1/2 bg-gray-900 p-8 flex justify-center items-center">
          <img 
            src="/Regi.png" // Replace this with your 3D image or abstract design
            alt="3D Abstract"
            className="w-full h-auto object-contain rounded-lg"
          />
        </div>

        {/* Login Window */}
        <div className="w-1/2 bg-gray-800 p-8 flex justify-center items-center">
          <div className="w-full max-w-md">
            <h2 className="text-3xl font-semibold text-white mb-6 text-center">Log in to your account</h2>
            <form>
              <div className="mb-4">
                <input
                  type="email"
                  placeholder="Email"
                  autoComplete="off" // Prevent autofill for email
                  className="w-full px-4 py-2 bg-gray-600 text-white rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
                />
              </div>
              <div className="mb-4">
                <input
                  type="password"
                  placeholder="Password"
                  autoComplete="off" // Prevent autofill for password
                  className="w-full px-4 py-2 bg-gray-600 text-white rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
                />
              </div>
              <button className="w-full bg-purple-600 text-white py-2 rounded hover:bg-purple-700 transition duration-200 mb-4">
                <a href="http://localhost:3000/">Login</a>
              </button>
            </form>

            <div className="mt-4 text-center">
              <p className="text-gray-400">Don't have an account? <NavLink to="/signup" className="text-purple-500 underline">Sign up</NavLink></p>
            </div>

            <div className="flex justify-center mt-4">
              <button className="w-1/2 bg-red-500 text-white py-2 rounded mr-2 hover:bg-red-600 transition duration-200">
                Google
              </button>
              <button className="w-1/2 bg-gray-500 text-white py-2 rounded hover:bg-gray-600 transition duration-200">
                Apple
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
