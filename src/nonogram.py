'''
Created on 2014/09/14

@author: alchu
'''

class Nonogram(object):
    def __init__(self):
        self._left = []
        self._top = []
        self._field = []
    
    def set_left(self, ary):
        self._left = ary
        
    def set_top(self, ary):
        
        self._top =ary
        
    def row(self):
        return len(self._left)
    
    def column(self):
        return len(self._top)
    
    def solve(self):
        '''stub'''
        self._field = [0,0]
    
    def _check_total(self):
        left_total = sum(map(sum, self._left))
        top_total = sum(map(sum, self._top))
        if left_total == top_total:
            return ""
        else:
            return "not match total left:top=%d:%d" % (left_total, top_total)
    
    def _line_len(self, prof):
        '''calculate minimum line length by profile list'''
        return sum(prof)+len(prof)-1
    
    def _check_profile(self):
        for d in self._left:
            if self._line_len(d) > len(self._top):
                return "profile over size"
        for d in self._top:
            if self._line_len(d) > len(self._left):
                return "profile over size"
        return ""
    
if __name__ == '__main__':
    pass