import unittest
from fuzzy_ops.fuzzy_set import _c1

class TestData(unittest.TestCase):
    def in_data(self):
        a = list(range(10))
        b = [0.1]
        c = list(range(10))
        self.assertRaises(ValueError, a,b,c)
        self.assertRaises(TypeError, 'a','a','a')
        
