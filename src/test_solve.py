'''
Created on 2014/09/15

@author: alchu
'''
import unittest
from nonogram import Nonogram

class Test(unittest.TestCase):


    def testInvader(self):
        left = [[3],
                [5],
                [2,1,2],
                [5],
                [3],
                [1,1],
                [1,1]]
        top = [[1],
               [3,1],
               [2,3],
               [5],
               [2,3],
               [3,1],
               [1]]
        n = Nonogram()
        n.set_left(left)
        n.set_top(top)
        n.solve()
        self.assertEqual(n._field, [])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()