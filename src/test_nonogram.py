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
        
    def test_constant(self):
        self.assertEqual(Nonogram.WHITE, 0)
        self.assertEqual(Nonogram.BLACK, 1)
        self.assertEqual(Nonogram.UNKNOWN, 2)

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

    def test_check_total(self):
        f = Nonogram()
        f.set_left([[1],[0]])
        f.set_top([[1]])
        msg = f._check_total()
        self.assertEqual(msg, "")
        
        f.set_left([[2],[1],[1]])
        f.set_top([[2],[1,1]])
        msg = f._check_total()
        self.assertEqual(msg, "")
        
        f.set_left([[1],[0]])
        f.set_top([[0]])
        msg = f._check_total()
        self.assertEqual(msg, "not match total left:top=1:0")
        
    def test_line_len(self):
        f = Nonogram()
        l = f._line_len([3])
        self.assertEqual(l, 3)
        l = f._line_len([1,2])
        self.assertEqual(l, 4)
        l = f._line_len([1,2,3,4])
        self.assertEqual(l, 13)
        
    def test_check_profile(self):
        f = Nonogram()
        
        f.set_left([[2],[1],[1]])
        f.set_top([[2],[1,1]])
        msg = f._check_profile()
        self.assertEqual(msg, "")
        
        f.set_left([[2],[1],[1]])
        f.set_top([[1],[2,1]])
        msg = f._check_profile()
        self.assertEqual(msg, "profile over size")
        
        f.set_left([[1],[2,1]])
        f.set_top([[2],[1],[1]])
        msg = f._check_profile()
        self.assertEqual(msg, "profile over size")
        
    def test_clear_field(self):
        f = Nonogram()
        
        f.set_left([[2],[1],[1]])
        f.set_top([[2],[1,1]])
        f._clear_field()
        n = f.row()*f.column()
        s = sum(map(sum, f._field))
        self.assertEqual(s, n*2)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()