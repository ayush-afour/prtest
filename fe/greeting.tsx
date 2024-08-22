// Greeting.tsx

import React from 'react';

// Define the props interface
interface GreetingProps {
  name: string;
  age: number;
}

// Define a functional component
const Greeting: React.FC<GreetingProps> = ({ name, age }) => {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
    </div>
  );
};

// Example usage of the Greeting component
const App: React.FC = () => {
  return (
    <div>
      <Greeting name="John Doe" age={30} />
    </div>
  );
};

export default App;
