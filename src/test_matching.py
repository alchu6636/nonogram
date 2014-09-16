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
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_create']
    unittest.main()
