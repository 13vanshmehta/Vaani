import React from 'react';
import "../index.css";

export const Dashboard = () => {
  return (
    <div className="flex min-h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-800 text-white p-4">
        <div className="flex items-center mb-8">
          <img src="/People/Pep-2.jpg" alt="" className='dash-img'/>
          <div className="ml-4">
            <h2 className="text-lg font-semibold">Vansh Mehta</h2>
          </div>
        </div>
        <nav className="space-y-4">
          <a href="#" className="block py-2 px-4 rounded bg-gray-700">Home</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Dashboard</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Inventory</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Campaigns Strategies</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Feedback</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Weather</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Festival</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">News</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Social Media</a>


        </nav>
        <div className="mt-8">
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Change Password</a>
          <a href="#" className="block py-2 px-4 hover:bg-gray-700">Log Out</a>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6">
        <h1 className="text-2xl font-semibold mb-4">Hello Vansh Mehta</h1>

        {/* Invoice and Credit Overview */}
        <div className="flex space-x-6 mb-6">
          <div className="bg-white p-4 rounded-lg shadow w-1/2">
            <h3 className="text-sm text-gray-500">OUTSTANDING INVOICES</h3>
            <p className="text-3xl font-semibold text-yellow-500">$231.53</p>
            <p className="text-sm text-gray-500">Number of Outstanding Invoices: 1</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow w-1/2">
            <h3 className="text-sm text-gray-500">AVAILABLE CREDITS</h3>
            <p className="text-3xl font-semibold text-green-500">$142.22</p>
          </div>
        </div>

        {/* Last Payment and Order Overview */}
        <div className="flex space-x-6 mb-6">
          <div className="bg-white p-4 rounded-lg shadow w-1/2">
            <h3 className="text-sm text-gray-500">Last Payment Made</h3>
            <p className="text-2xl font-semibold">$198.45</p>
            <p className="text-sm text-gray-500">Paid for <a href="#" className="text-blue-500 underline">INV-000010</a> on 04 Jul 2022</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow w-1/2">
            <h3 className="text-sm text-gray-500">Sales Order Overview</h3>
            <div className="flex space-x-4 mt-2 text-center">
              <div>
                <p className="text-xl font-semibold">0</p>
                <p className="text-sm text-gray-500">Unconfirmed</p>
              </div>
              <div>
                <p className="text-xl font-semibold">1</p>
                <p className="text-sm text-gray-500">Not Packed</p>
              </div>
              <div>
                <p className="text-xl font-semibold">0</p>
                <p className="text-sm text-gray-500">Not Shipped</p>
              </div>
              <div>
                <p className="text-xl font-semibold">1</p>
                <p className="text-sm text-gray-500">Pending Delivery</p>
              </div>
            </div>
          </div>
        </div>

        {/* My Details and Shared Documents */}
        <div className="flex space-x-6">
          <div className="bg-white p-4 rounded-lg shadow w-1/2">
            <h3 className="text-sm text-gray-500">My Details</h3>
            <p className="text-lg font-semibold">Vansh Mehta</p>
            <a href="#" className="text-blue-500 underline text-sm">View More</a>
          </div>
          <div className="bg-white p-4 rounded-lg shadow w-1/2">
            <h3 className="text-sm text-gray-500">Shared Documents</h3>
            <div className="flex items-center justify-center border-2 border-dashed border-gray-300 rounded-lg h-32 mt-2">
              <p className="text-center text-sm text-gray-500">Documents that are shared between you and Zylker Fashions will appear here.</p>
            </div>
            <a href="#" className="text-blue-500 underline text-sm block mt-2">Upload Documents</a>
          </div>
        </div>
      </main>
    </div>
  );
};

