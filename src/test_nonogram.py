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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()