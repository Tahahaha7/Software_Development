import unittest

class ClockIterator():
    def __init__(self):
        self.h, self.m = 0, 0
        self.counter = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 2000:
            if self.m%60 == 59:
                self.h+=1
            self.m+=1
            self.counter += 1
            return str(self.h%24).zfill(2)+":"+str(self.m%60).zfill(2)
        else:
            raise StopIteration
            
    def storing(self, idx):
        store = ['00:00']
        for i in self:
            store.append(i)
        return store[idx-1]

clock = ClockIterator()

class TestStr(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(clock.storing(1441), "00:00")
    def test2(self):
        self.assertEqual(clock.storing(61), "01:00")
if __name__ == '__main__':
    unittest.main()