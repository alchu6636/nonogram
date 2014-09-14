'''
Created on 2014/09/14

@author: alchu
'''
import unittest
from nonogram import Nonogram 

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_create(self):
        f = Nonogram()
        self.assertNotEqual(f, False)

    def test_set_left(self):
        f = Nonogram()
        self.assertEqual(f.row(), 0)
        f.set_left([[0],[0]])
        self.assertEqual(f.row(), 2)
        
    def test_set_top(self):
        f = Nonogram()
        self.assertEqual(f.column(), 0)
        f.set_top([[0],[0],[0]])
        self.assertEqual(f.column(), 3)

    def test_solve(self):
        f = Nonogram()
        f.set_left([[0],[0]])
        f.set_top([[0]])
        self.assertEqual(f._field, [])
        f.solve()
        self.assertEqual(f._field, [0,0])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()