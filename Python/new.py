# File: example.py

# Function outside the class
def greet(name):
    print(f"Hello, {name}!")

# Class definition
class Calculator:
    # Constructor method
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Method inside the class
    def add(self):
        return self.a + self.b

    # Another method inside the class
    def multiply(self):
        return self.a * self.b

# Code not inside a method (will run when the file is executed)
if __name__ == "__main__":
    # Function call
    greet("Alice")

    # Create an instance of Calculator
    calc = Calculator(10, 20)

    # Call methods on the instance
    print("Addition:", calc.add())
    print("Multiplication:", calc.multiply())
