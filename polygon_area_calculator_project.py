"""
Module that defines Rectangle and Square classes
and demonstrates basic geometric operations.
"""
class Rectangle:
    """ A class representing a rectangle shape, defined by its width and height. """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """Set the width of the rectangle."""
        self.width = width

    def set_height(self, height):
        """Set the height of the rectangle."""
        self.height = height

    def get_area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Calculate and return the diagonal length of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Return a string that represents the shape of the rectangle using lines of "*". 
        If the width or height is larger than 50, return a message saying 
        'it's too big for a picture.'"""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        """Calculate and return the number of times the passed in shape 
        could fit inside the current shape. 
        The shape passed in will be an instance of Rectangle or Square."""
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    """ A class representing a square shape, 
    which is a special case of a rectangle where the width and height are equal. """

    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        """Set the side length of the square, 
        which also sets the width and height to the same value."""
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
