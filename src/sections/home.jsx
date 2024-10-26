import React from 'react';
import { LineChart, Line, XAxis, YAxis, ResponsiveContainer } from 'recharts';
import { Wand2 } from 'lucide-react';
import { NavLink } from 'react-router-dom';
import "../index.css";
// Import your images for integrations
import wordpressLogo from '../assets/wordpress.png';
import wixLogo from '../assets/wix.png';
import shopifyLogo from '../assets/shopify.png';
import squarespaceLogo from '../assets/squarespace.png';
import mediumLogo from '../assets/medium.png';
import twitterLogo from '../assets/twitter.png';
import facebookLogo from '../assets/facebook.png';
import mailchimpLogo from '../assets/mailchimp.png';
// Add more imports for additional integration logos

export const Home = () => {
  const chartData = [
    { name: '10', value1: 100, value2: 120 },
    { name: '15', value1: 150, value2: 140 },
    { name: '20', value1: 180, value2: 190 },
    { name: '25', value1: 200, value2: 180 },
    { name: '30', value1: 220, value2: 240 },
    { name: '05', value1: 250, value2: 230 },
    { name: '10', value1: 280, value2: 270 }
  ];

  const companyLogos = [
    '/brands/logo1.png',
    '/brands/logo2.png',
    '/brands/logo3.png',
    '/brands/logo4.png',
    '/brands/logo5.png',
    '/brands/logo6.png'
  ];

  // Array of 8-10 integration images
  const integrations = [
    { name: 'Wordpress', logo: wordpressLogo },
    { name: 'Wix', logo: wixLogo },
    { name: 'Shopify', logo: shopifyLogo },
    { name: 'Squarespace', logo: squarespaceLogo },
    { name: 'Medium', logo: mediumLogo },
    { name: 'Twitter', logo: twitterLogo },
    { name: 'Facebook', logo: facebookLogo },
    { name: 'Mailchimp', logo: mailchimpLogo },
    // Add more integrations as needed
  ];

  return (
    <div className="min-h-screen bg-black text-white p-8 Main-Body">

      {/* Trust Badge */}
      <div className="flex justify-center mb-8">
        <div className="flex items-center gap-2 text-sm text-gray-400">
          <div className="flex -space-x-2">
            <img src="/People/Pep-1.jpg" alt="user" className="w-8 h-8 rounded-full border-2 border-black" />
            <img src="/People/Pep-2.jpg" alt="user" className="w-8 h-8 rounded-full border-2 border-black" />
            <img src="/People/Pep-3.jpg" alt="user" className="w-8 h-8 rounded-full border-2 border-black" />
          </div>
          <span>Trusted by 35,000+ people</span>
        </div>
      </div>

      {/* Hero Section */}
      <div className="max-w-4xl mx-auto text-center mb-12">
        <h1 className="text-7xl font-bold mb-6 bg-gradient-to-r from-white to-gray-600 bg-clip-text text-transparent">
          Managing your content with AI
        </h1>
        <br />
        <p className="text-gray-400 text-xl mb-8">
          An open source content management system that uses AI to automate 
          various aspects of content creation, optimization, and distribution.
        </p>
        <button className="px-6 py-3 bg-white text-black rounded-full font-medium hover:bg-gray-100 transition-colors">
        <NavLink to = "/signup">Get started for free</NavLink>
        </button>
      </div>

      {/* Dashboard Preview */}
      <div className="max-w-5xl mx-auto bg-[#111111] rounded-2xl p-6">
        {/* Tab Bar */}
        <div className="flex gap-4 mb-6">
          <button className="flex items-center gap-2 px-4 py-2 bg-[#222222] rounded-lg text-sm">
            <Wand2 className="w-4 h-4" />
            Create Content
          </button>
          <button className="flex items-center gap-2 px-4 py-2 text-gray-400 rounded-lg text-sm">
            Content Optimization
          </button>
          <button className="flex items-center gap-2 px-4 py-2 text-gray-400 rounded-lg text-sm">
            Distribute
          </button>
          <button className="flex items-center gap-2 px-4 py-2 text-gray-400 rounded-lg text-sm ml-auto">
            •••
          </button>
        </div>

        {/* Content Area */}
        <div className="flex gap-6">
          {/* Stats Card */}
          <div className="bg-[#1A1A1A] rounded-xl p-4 w-64">
            <div className="mb-4">
              <div className="text-sm text-gray-400">Total Traffic</div>
              <div className="text-2xl font-bold">240.8K*</div>
            </div>
            <div className="h-32">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={chartData}>
                  <Line type="monotone" dataKey="value1" stroke="#ff4d4d" strokeWidth={2} dot={false} />
                  <Line type="monotone" dataKey="value2" stroke="#666" strokeWidth={2} dot={false} />
                  <XAxis dataKey="name" stroke="#666" />
                  <YAxis stroke="#666" />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Main Content */}
          <div className="flex-1">
            <p className="text-gray-400 mb-4">
              Time management is a crucial skill that can greatly improve productivity and reduce stress in
              both personal and professional life. Effective time management involves organizing and plann
              ing wisely, prioritizing tasks, setting goals, and avoiding distr...
            </p>
            
            {/* Content Tools */}
            <div className="flex justify-between items-center">
              <div className="flex gap-3">
                <button className="p-2 bg-[#222222] rounded-lg">
                  <Wand2 className="w-4 h-4" />
                </button>
                {/* Add more tool buttons as needed */}
              </div>
              <button className="px-4 py-2 bg-white text-black rounded-lg flex items-center gap-2">
                <Wand2 className="w-4 h-4" />
                Generate text
              </button>
            </div>
          </div>

          {/* Sidebar */}
          <div className="w-48">
            <div className="text-sm font-medium mb-4">Create Content</div>
            <div className="space-y-3">
              <button className="flex items-center gap-2 text-gray-400 text-sm w-full">
                <Wand2 className="w-4 h-4" />
                Text generation
              </button>
              <button className="flex items-center gap-2 text-gray-400 text-sm w-full">
                <Wand2 className="w-4 h-4" />
                Content Ideas
              </button>
              <button className="flex items-center gap-2 text-gray-400 text-sm w-full">
                <Wand2 className="w-4 h-4" />
                Scheduling
              </button>
            </div>
          </div>
        </div>
      </div>

      <br />
      
      {/* Company Logos Section */}
      <div className="flex justify-center mb-6 space-x-10">
        {companyLogos.map((logo, index) => (
          <img key={index} src={logo} alt={`Company Logo ${index + 1}`} className="w-26 h-20" />
        ))}
      </div>

      <br />

      {/* Integrations Section */}
      <div className="text-center mb-10">
        <h2 className="text-7xl font-bold mb-7 bg-gradient-to-r from-white to-gray-700 bg-clip-text text-transparent">
          Integrations and Extensibility
        </h2>
        <p className="text-gray-400 mb-6">
          Integrate seamlessly with social media platforms for automatic posting and interaction analysis, and extend functionality through plugins and APIs for analytics and email newsletters.
        </p>
        {/* Grid for 8-10 logos */}
        <div className="grid grid-cols-4 gap-8 max-w-5xl mx-auto">
          {integrations.map((integration, index) => (
            <div key={index} className="flex flex-col items-center">
              <img src={integration.logo} alt={`${integration.name} Logo`} className="w-16 h-16 mb-2 white-logo" />
              <p className="text-gray-400">{integration.name}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
