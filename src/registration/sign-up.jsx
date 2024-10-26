import React from 'react';
import { NavLink } from 'react-router-dom';

export const Signup = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-web">
      {/* Combined Section with Slightly Different Background Colors */}
      <div className="flex w-full max-w-5xl rounded-lg shadow-2xl overflow-hidden lg:flex-row flex-col bg-gray-900">
        {/* 3D Abstract/Image Div */}
        <div className="lg:w-1/2 w-full flex justify-center items-center bg-gray-700 p-10">
          <div className="rounded-lg">
            <img 
              src="/Regi.png" // Replace this with your 3D image or abstract design
              alt="3D Abstract"
              className="rounded-lg"
              height="500px"
              width="500px"
            />
          </div>
        </div>

        {/* Signup Window */}
        <div className="lg:w-1/2 w-full flex justify-center items-center bg-gray-800 p-10">
          <div className="w-full max-w-lg">
            <h2 className="text-3xl font-semibold text-white mb-6 text-center">Create an account</h2>
            <form>
              <div className="mb-4">
                <input
                  type="text"
                  placeholder="First Name"
                  className="w-full px-4 py-2 bg-gray-600 text-white rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
                />
              </div>
              <div className="mb-4">
                <input
                  type="text"
                  placeholder="Last Name"
                  className="w-full px-4 py-2 bg-gray-600 text-white rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
                />
              </div>
              <div className="mb-4">
                <input
                  type="email"
                  placeholder="Email"
                  className="w-full px-4 py-2 bg-gray-600 text-white rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
                />
              </div>
              <div className="mb-4">
                <input
                  type="password"
                  placeholder="Enter your password"
                  className="w-full px-4 py-2 bg-gray-600 text-white rounded focus:outline-none focus:ring-2 focus:ring-purple-500"
                />
              </div>
              <div className="mb-4 flex items-center">
                <input type="checkbox" className="mr-2" />
                <span className="text-gray-400">I agree to the <a href="#" className="text-purple-500 underline">Terms & Conditions</a></span>
              </div>
              <button className="w-full bg-purple-600 text-white py-2 rounded hover:bg-purple-700 transition duration-200">
                Create account
              </button>
            </form>

            <div className="mt-4 text-center">
              <p className="text-gray-400">Already have an account? <NavLink to="/login" className="text-purple-500 underline">Log in</NavLink></p>
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
