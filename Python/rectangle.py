# rectangle.py

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

# Create a rectangle object
rect = Rectangle(5.0, 10.0)

# Calculate and print the area
print(f"The area of the rectangle is: {rect.area()} square units")