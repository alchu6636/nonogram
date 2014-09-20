'''
Created on 2014/09/16

@author: alchu
'''
import unittest
from nonogram import Nonogram, LineMaker, PosIter

BK = Nonogram.BLACK
WT = Nonogram.WHITE
UN = Nonogram.UNKNOWN

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
        
class TestLineMaker(unittest.TestCase):
    def test_create(self):
        LineMaker([1], 2)
        
    def test_next(self):
        lm = LineMaker([1], 2)
        expect = [[BK,WT],
                  [WT,BK]
                  ]
        while expect:
            self.assertEqual(lm.next(), expect.pop(0))
        self.assertEqual(lm.next(), None)

    def test_next39(self):        
        lm = LineMaker([2,1,2], 9)
        expect = [[BK,BK,WT,BK,WT,BK,BK,WT,WT],
                  [WT,BK,BK,WT,BK,WT,BK,BK,WT],
                  [WT,WT,BK,BK,WT,BK,WT,BK,BK],
                  [BK,BK,WT,WT,BK,WT,BK,BK,WT],
                  [WT,BK,BK,WT,WT,BK,WT,BK,BK],
                  [BK,BK,WT,WT,WT,BK,WT,BK,BK],
                  [BK,BK,WT,BK,WT,WT,BK,BK,WT],
                  [WT,BK,BK,WT,BK,WT,WT,BK,BK],
                  [BK,BK,WT,WT,BK,WT,WT,BK,BK],
                  [BK,BK,WT,BK,WT,WT,WT,BK,BK],
                  ]
        while expect:
            self.assertEqual(lm.next(), expect.pop(0))
        self.assertEqual(lm.next(), None)
        
    def test_postotal(self):
        data = [[[1], 1, 0],
                [[1], 2, 1],
                [[2], 3, 1],
                [[1,1], 3, 0],
                [[1,1], 4, 1],
                [[2,3], 8, 2],
                [[3,2,2], 10, 1],
                [[1,1,1], 5, 0]
                ]
        while data:
            prof, width, expect = data.pop(0)
            lm = LineMaker(prof, width)
            self.assertEqual(lm._postotal(), expect)
            
    def test_pos2line(self):
        lm = LineMaker([2,2], 6)
        line = lm._pos2line([0,0])
        self.assertEqual(line, [BK,BK,WT,BK,BK,WT])
        line = lm._pos2line([1,0])
        self.assertEqual(line, [WT,BK,BK,WT,BK,BK])
        line = lm._pos2line([0,1])
        self.assertEqual(line, [BK,BK,WT,WT,BK,BK])
        
    def test_is_fit(self):
        n = Nonogram()
        self.assertEqual(n._is_fit([UN,WT,BK,UN], [WT,WT,BK,WT]), True)
        self.assertEqual(n._is_fit([UN,WT,UN], [WT,BK,WT]), False)
        self.assertEqual(n._is_fit([UN,BK,UN], [WT,WT,WT]), False)
        
    def test_line_or(self):
        n = Nonogram()
        self.assertEqual(n._line_or([WT,BK,BK],[BK,BK,WT]), [UN,BK,UN])
        self.assertEqual(n._line_or([UN,BK,UN],[WT,BK,BK]), [UN,BK,UN])
        
    def test_line_match(self):
        n = Nonogram()
        prof = [1]
        data = [[[UN,UN], [UN,UN]],
                [[UN,BK], [WT,BK]],
                [[BK,UN], [BK,WT]],
                [[UN,WT], [BK,WT]],
                [[WT,UN], [WT,BK]]
                ]
        while data:
            (f, expect) = data.pop(0)
            result = n._line_match(f, prof)
            self.assertEqual(result, expect)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_create']
    unittest.main()
