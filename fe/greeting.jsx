// Greeting.jsx

import React from 'react';

// Define a functional component
const Greeting = ({ name }) => {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>Welcome to our site.</p>
    </div>
  );
};

// Example usage of the Greeting component
const App = () => {
  return (
    <div>
      <Greeting name="John Doe" />
    </div>
  );
};

export default App;
