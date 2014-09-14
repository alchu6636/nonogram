'''
Created on 2014/09/14

@author: alchu
'''

class Nonogram(object):
    WHITE = 0
    BLACK = 1
    UNKNOWN = 2
    
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
    
    def _clear_field(self):
        '''fill all cell in field by UNKNOWN'''
        self._field = [[Nonogram.UNKNOWN for col in range(self.column())] for row in range(self.row())]
    
    def _pickup_row(self, pos):
        return self._field[pos]
    
    def _pickup_column(self, pos):
        d = [r[pos] for r in self._field]
        return d
    
    def _check_update(self, before, after):
        if before == Nonogram.BLACK and after == Nonogram.WHITE:
            raise ValueError
        if before == Nonogram.WHITE and after == Nonogram.BLACK:
            raise ValueError
        
    def _pickdown_row(self, pos, ar):
        self._field[pos] = ar
    
    def _pickdown_column(self, pos, ar):
        for row in self._field:
            row[pos] = ar.pop(0)
            
    
if __name__ == '__main__':
    pass
