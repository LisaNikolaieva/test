import unittest
from main import Coord, line_length

class TesTLineLength(unittest.TestCase):

    def test_ut1(self):
        a1 = Coord(1, 1)
        a2 = Coord(2, 1)
        self.assertEqual(1, line_length(a1, a2))

    def test_ut2(self):
        a1 = Coord(1, 1)
        a2 = Coord(-2, -3)
        self.assertEqual(5, line_length(a1, a2))

    def test_ut3(self):
        a1 = Coord(1, 1)
        a2 = Coord(1, 0)
        self.assertEqual(1, line_length(a1, a2))

    def test_ut4(self):
        a1 = Coord(1, 1)
        a2 = Coord(-3, -2)
        self.assertEqual(5, line_length(a1, a2))

    def test_ut5(self):
        a1 = Coord(1, 1)
        a2 = Coord(0, 1)
        self.assertEqual(1, line_length(a1, a2))

    def test_ut6(self):
        a1 = Coord(1, 1)
        a2 = Coord(5, 4)
        self.assertEqual(5, line_length(a1, a2))

    def test_ut7(self):
        a1 = Coord(1, 1)
        a2 = Coord(5, -2)
        self.assertEqual(5, line_length(a1, a2))

    def test_ut8(self):
        a1 = Coord(1, 1)
        a2 = Coord(4, 5)
        self.assertEqual(5, line_length(a1, a2))


    def test_ut9(self):
        a1 = Coord(1, 1)
        a2 = Coord(-1, 1)
        self.assertEqual(2, line_length(a1, a2))

    def test_ut10(self):
        a1 = Coord(1, 1)
        a2 = Coord(1, -1)
        self.assertEqual(2, line_length(a1, a2))

    def test_ut11(self):
        a1 = Coord(3, 4)
        a2 = Coord(-3, -4)
        self.assertEqual(10, line_length(a1, a2))