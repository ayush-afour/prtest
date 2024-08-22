// greet.ts

// Define an interface for a Person
interface Person {
    firstName: string;
    lastName: string;
    age: number;
}

// Function to greet a person
function greet(person: Person): string {
    return `Hello, ${person.firstName} ${person.lastName}! You are ${person.age} years old.`;
}

// Create a person object
const person: Person = {
    firstName: "John",
    lastName: "Doe",
    age: 25
};

// Call the greet function and log the result
console.log(greet(person));
