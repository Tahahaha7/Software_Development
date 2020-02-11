import unittest
from clock_iterator import ClockIterator

clock = ClockIterator()

class TestStr(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(clock.storing(1), "00:00")
"""
    def test2(self):
        self.assertEqual(clock.storing(60), "00:59")
        
    def test3(self):
        self.assertEqual(clock.storing(61), "01:00")
    
    def test4(self):
        self.assertEqual(clock.storing(1440), "23:59")
    
    def test5(self):
        self.assertEqual(clock.storing(1441), "00:00")
"""
if __name__ == '__main__':
    unittest.main()