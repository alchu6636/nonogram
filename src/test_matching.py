'''
Created on 2014/09/16

@author: alchu
'''
import unittest
from nonogram import PosIter

class TestPosIter(unittest.TestCase):

    def test_create(self):
        PosIter(2, 0)

    def _nexts(self, pos, expects):
        while expects:
            self.assertEqual(pos.next(), expects.pop(0))
        self.assertEqual(pos.next(), None)
            
    def test_next10(self):
        p = PosIter(1, 0)
        self._nexts(p, [[0]])
        
    def test_next11(self):
        p = PosIter(1, 1)
        self._nexts(p, [[0],
                       [1]])
        
    def test_next12(self):
        p = PosIter(1, 2)
        self._nexts(p, [[0],
                       [1],
                       [2]])
    
    def test_next20(self):
        p = PosIter(2, 0)
        self._nexts(p, [[0,0]])
        
    def test_next21(self):
        p = PosIter(2, 1)
        self._nexts(p, [[0,0],
                        [1,0],
                        [0,1]])
        
    def test_next22(self):
        p = PosIter(2, 2)
        self._nexts(p, [[0,0],
                        [1,0],
                        [2,0],
                        [0,1],
                        [1,1],
                        [0,2]])
        
    def test_next32(self):
        p = PosIter(3, 2)
        self._nexts(p, [[0,0,0],
                        [1,0,0],
                        [2,0,0],
                        [0,1,0],
                        [1,1,0],
                        [0,2,0],
                        [0,0,1],
                        [1,0,1],
                        [0,1,1],
                        [0,0,2]])
        
    def test_is_last(self):
        p = PosIter(2, 1)
        p.next()
        self.assertEqual(p._is_last(), False)
        p.next()
        self.assertEqual(p._is_last(), False)
        p.next()
        self.assertEqual(p._is_last(), True)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_create']
    unittest.main()
