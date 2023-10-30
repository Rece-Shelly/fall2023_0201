import unittest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class TestRectangle(unittest.TestCase):
    def test_get_area(self):
        rectangle_1 = Rectangle(2, 3)
        self.assertEqual(rectangle_1.get_area(), 6, "Area is calculated wrong")
    
    def test_perimeter(self):
        rectangle_1 = Rectangle(2, 3)
        self.assertEqual(rectangle_1.get_perimeter(), 10, "Perimeter is calculated wrong")

# run the test
unittest.main()