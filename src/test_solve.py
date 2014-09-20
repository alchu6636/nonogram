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
        expect = [[0, 0, 1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [1, 1, 0, 1, 0, 1, 1],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0]]
        n = Nonogram()
        n.set_left(left)
        n.set_top(top)
        n.solve()
        self.assertEqual(n._field, expect)
        
    def test28943(self):
        '''
        http://www.minicgi.net/logic/logic.html?num=28943
        '''
        left = [[12],
                [12],
                [1,1,1,1],
                [12],
                [12],
                [1,1,1,1],
                [12],
                [13],
                [12,2],
                [2,2,2,2],
                [2,2,2,2],
                [2,2],
                [2,2]
                ]
        top = [[1],
               [5],
               [6],
               [2],
               [2,2,5],
               [11],
               [2,2,3],
               [2,2,3],
               [9],
               [2,2,7],
               [2,2,7],
               [9],
               [2,2,2],
               [2,2,5],
               [11],
               [2,2,1]
               ]
        expect = []
        n = Nonogram()
        n.set_left(left)
        n.set_top(top)
        n.solve()
        self.assertEqual(n._field, expect)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()