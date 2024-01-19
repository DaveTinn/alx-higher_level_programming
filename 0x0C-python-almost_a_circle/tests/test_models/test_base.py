import sys
import os
import unittest
from tests.test_models.test_base import TestRectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 3)

    def test_width(self):
        rect = Rectangle(5, 10)
        rect.width = 20
        self.assertEqual(rect.width, 20)

    def test_height(self):
        rect = Rectangle(5, 10)
        rect.height = 15
        self.assertEqual(rect.height, 15)

    def test_x(self):
        rect = Rectangle(5, 10)
        rect.x = 2
        self.assertEqual(rect.x, 2)

    def test_y(self):
        rect = Rectangle(5, 10)
        rect.y = 3
        self.assertEqual(rect.y, 3)

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -1, 2)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 1, -2)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("5", 10)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "10")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, "1", 2)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 1, "2")

if __name__ == '__main__':
    unittest.main()
