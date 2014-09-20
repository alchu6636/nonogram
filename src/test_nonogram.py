'''
Created on 2014/09/14

@author: alchu
'''
import unittest
from nonogram import Nonogram, _read_profile

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
        self.assertEqual(f.len_row(), 0)
        f.set_left([[0],[0]])
        self.assertEqual(f.len_row(), 2)
        
    def test_set_top(self):
        f = Nonogram()
        self.assertEqual(f.len_column(), 0)
        f.set_top([[0],[0],[0]])
        self.assertEqual(f.len_column(), 3)

    def test_solve(self):
        f = self._create_pat32()
        f.solve()
        self.assertEqual(f._field, [[1,1],
                                    [1,0],
                                    [0,1]])
        f = Nonogram()
        f.set_left([[2], [1, 1]])
        f.set_top([[2], [1], [1]])
        f.solve()
        self.assertEqual(f._field, [[1,1,0],
                                    [1,0,1]])

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
        

    def _create_pat32(self):
        f = Nonogram()
        f.set_left([[2], [1], [1]])
        f.set_top([[2], [1, 1]])
        return f

    def test_check_profile(self):
        f = self._create_pat32()
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
        f = self._create_pat32()
        f._clear_field()
        n = f.len_row()*f.len_column()
        s = sum(map(sum, f._field))
        self.assertEqual(s, n*2)
        
    def test_pickup(self):
        f = self._create_pat32()
        f._clear_field()
        f._field[2][1] = 0
        d = f._pickup_row(2)
        self.assertEqual(d, [2,0])
        c = f._pickup_column(1)
        self.assertEqual(c, [2,2,0])
        
    def test_check_update(self):
        f = Nonogram()
        f._check_update(Nonogram.UNKNOWN, Nonogram.WHITE)
        f._check_update(Nonogram.UNKNOWN, Nonogram.BLACK)
        with self.assertRaises(ValueError):
            f._check_update(Nonogram.WHITE, Nonogram.BLACK)
        with self.assertRaises(ValueError):
            f._check_update(Nonogram.BLACK, Nonogram.WHITE)

    def test_pickdown(self):
        f = self._create_pat32()
        f._clear_field()
        f._pickdown_row(1, [Nonogram.WHITE,Nonogram.BLACK])
        r = f._pickup_column(0)
        self.assertEqual(r, [Nonogram.UNKNOWN,
                             Nonogram.WHITE,
                             Nonogram.UNKNOWN])
        with self.assertRaises(ValueError):
            f._pickdown_row(1, [Nonogram.WHITE,Nonogram.WHITE])

        
        f._pickdown_column(0, [Nonogram.WHITE,
                               Nonogram.WHITE,
                               Nonogram.BLACK])
        r = f._pickup_row(0)
        self.assertEqual(r, [Nonogram.WHITE, Nonogram.UNKNOWN])
        with self.assertRaises(ValueError):
            f._pickdown_column(0, [Nonogram.WHITE]*3)
        
    def test_picdown_row_unknown(self):
        f = self._create_pat32()
        f._clear_field()
        f._pickdown_row(0, [Nonogram.UNKNOWN, Nonogram.BLACK])
        f._pickdown_row(0, [Nonogram.WHITE, Nonogram.UNKNOWN])
        r = f._pickup_row(0)
        self.assertEqual(r, [Nonogram.WHITE, Nonogram.BLACK])
        
    def test_picdown_column_unknown(self):
        f = self._create_pat32()
        f._clear_field()
        f._pickdown_column(0, [Nonogram.UNKNOWN, Nonogram.BLACK, Nonogram.UNKNOWN])
        f._pickdown_column(0, [Nonogram.WHITE, Nonogram.UNKNOWN, Nonogram.UNKNOWN])
        r = f._pickup_column(0)
        self.assertEqual(r, [Nonogram.WHITE, Nonogram.BLACK, Nonogram.UNKNOWN])

    def test_line2field(self):
        f = Nonogram()
        
        fld = f._line2field([3])
        self.assertEqual(fld, [Nonogram.BLACK]*3)
        fld = f._line2field([1,1])
        self.assertEqual(fld, [Nonogram.BLACK,Nonogram.WHITE,Nonogram.BLACK])
        fld = f._line2field([1,2,1])
        self.assertEqual(fld, [Nonogram.BLACK,Nonogram.WHITE,Nonogram.BLACK,
                               Nonogram.BLACK,Nonogram.WHITE,Nonogram.BLACK])

    def test_slide_line(self):    
        WT = Nonogram.WHITE
        BK = Nonogram.BLACK
        UN = Nonogram.UNKNOWN
        f = Nonogram()

        fld = f._slide_line([2], 2)
        self.assertEqual(fld, [BK, BK])
    
        fld = f._slide_line([2], 3)
        self.assertEqual(fld, [UN, BK, UN])
        
        fld = f._slide_line([2], 4)
        self.assertEqual(fld, [UN]*4)
       
        fld = f._slide_line([3,1], 5)
        self.assertEqual(fld, [BK,BK,BK,WT,BK])
        
        fld = f._slide_line([3,1], 6)
        self.assertEqual(fld, [UN,BK,BK,UN,UN,UN])
        
        fld = f._slide_line([3,1], 7)
        self.assertEqual(fld, [UN,UN,BK,UN,UN,UN,UN])
        
    def test_repr_field(self):
        f = self._create_pat32()
        f._field = [[1,0,2],
                    [1,1,0]]
        result = f._repr_field()
        self.assertEqual(result, ["WW  .  ?","WW WW  ."])
        
    def test_repr_left(self):
        f = Nonogram()
        f.set_left([[1],[1,2]])
        result = f._repr_left()
        self.assertEqual(result, ["  1","1 2"])
        
    def test_repf_top(self):
        f = Nonogram()
        f.set_top([[1],[3,2]])
        result = f._repr_top()
        self.assertEqual(result, ["    3"," 1  2"])
        
    def test_repr(self):
        f = self._create_pat32()
        f.solve()
        result = f.repr()
        self.assertEqual(len(result), 47)
        
    def test_read_profile(self):
        fobj = open('test1.dat', 'rb')
        prof = _read_profile(fobj)
        self.assertEqual(len(prof), 2)
        self.assertEqual(prof[0], [[1,10,1],[2,2]])
        self.assertEqual(prof[1], [[2],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2]])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
