import math

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def display_info(self):
        print(f'Color of this shape is {self.color}')
        print(f'This shape is {self.filled}')

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    
    def calculate_area(self):
        print(f'Area of circle is {math.pi * pow(self.radius, 2)}')

class Rectangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    
    def calculate_area(self):
        print(f'Area of rectnagle is {self.width * self.height}')


shape = Shape('color', 'filled status')
circle = Circle('blue', 'filled', 2)
rectangle = Rectangle('pink', 'not filled', 5, 2)

circle.display_info()
rectangle.display_info()
rectangle.calculate_area()
circle.calculate_area()
