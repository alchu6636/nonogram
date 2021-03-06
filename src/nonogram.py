'''
Created on 2014/09/14

@author: alchu
'''

import copy
import csv
import argparse

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
        
    def len_row(self):
        return len(self._left)
    
    def len_column(self):
        return len(self._top)
    
    def solve(self):
        self._check_profile()
        self._clear_field()
        for r in range(self.len_row()):
            self._solve_row_slide(r)
        for c in range(self.len_column()):
            self._solve_column_slide(c)    
        for n in range(100):
            prev = copy.deepcopy(self._field)
            for r in range(self.len_row()):
                self._solve_row_match(r)
            for c in range(self.len_column()):
                self._solve_column_match(c)    
            if prev == self._field:
                break
            
    def _solve_row_slide(self, row):
        line = self._slide_line(self._left[row], self.len_column())
        self._pickdown_row(row, line)
    
    def _solve_column_slide(self, col):
        line = self._slide_line(self._top[col], self.len_row())
        self._pickdown_column(col, line)

    def _solve_row_match(self, row):
        line = self._pickup_row(row)
        result = self._line_match(line, self._left[row])
        self._pickdown_row(row, result)

    def _solve_column_match(self, column):
        line = self._pickup_column(column)
        result = self._line_match(line, self._top[column])
        self._pickdown_column(column, result)

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
        self._field = [[Nonogram.UNKNOWN for col in range(self.len_column())] for row in range(self.len_row())]
    
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
        if after == Nonogram.UNKNOWN:
            return False
        else:
            return True
        
    def _pickdown_row(self, pos, ar):
        row = self._field[pos]
        for idx in range(len(row)):
            if self._check_update(row[idx], ar[0]):
                row[idx] = ar.pop(0)
            else:
                ar.pop(0)
    
    def _pickdown_column(self, pos, ar):
        for row in self._field:
            if self._check_update(row[pos], ar[0]):
                row[pos] = ar.pop(0)
            else:
                ar.pop(0)
          
    def _line2field(self, line):
        result = []
        while len(line)>0:
            result.extend([Nonogram.BLACK]*line[0])
            if len(line)>1:
                result.append(Nonogram.WHITE)
            line.pop(0)
        return result
    
    def _slide_line(self, linep, length):
        line = linep[:]
        margin = length - self._line_len(line)
        result = []
        while len(line)>0:
            unknownlen = min(line[0], margin)
            result.extend([Nonogram.UNKNOWN]*unknownlen)
            result.extend([Nonogram.BLACK]*(line[0]-unknownlen))
            if len(line)>1:
                if margin > 0:
                    result.append(Nonogram.UNKNOWN)
                else:
                    result.append(Nonogram.WHITE)
            line.pop(0)
        result.extend([Nonogram.UNKNOWN]*margin)    
        return result

    def _is_fit(self, field, trial):
        for (f,t) in zip(field, trial):
            if f == Nonogram.BLACK and t == Nonogram.WHITE:
                return False
            if f == Nonogram.WHITE and t == Nonogram.BLACK:
                return False
        return True
    
    def _line_or(self, linea, lineb):
        result = []
        for (a, b) in zip(linea, lineb):
            if a == b:
                result.append(a)
            else:
                result.append(Nonogram.UNKNOWN)
        return result
    
    def _line_match(self, line, prof):
        lm = LineMaker(prof, len(line))
        current = []
        while True:
            buf = lm.next()
            if not buf:
                break
            if self._is_fit(line, buf):
                if current:
                    current = self._line_or(current, buf)
                else:
                    current = buf
        return current
    
    def _field_str(self, data):
        if data == Nonogram.BLACK:
            return "WW"
        if data == Nonogram.WHITE:
            return " ."
        return " ?"
    
    def _repr_field(self):
        buf = []
        for row in self._field:
            point = map(lambda x:self._field_str(x), row)
            buf.append(" ".join(point))
        return buf
    
    def _repr_left(self):
        buf = []
        for prof in self._left:
            buf.append(" ".join(map(str, prof)))
        maxlen = max(map(len, buf))
        buf = map(lambda x:" "*maxlen+x, buf)
        buf = map(lambda x:x[-maxlen:], buf)
        return buf
        
    def _repr_top(self):
        maxlen = max(map(len, self._top))
        buf = []
        for prof in self._top:
            temp = map(lambda x:"%2d" % x, prof)
            temp = ["  "]*maxlen+temp
            temp = temp[-maxlen:]
            buf.append(temp)
        buf2 = [[r[col] for r in buf] for col in range(len(buf[0]))]
        buf2 = map(lambda x:" ".join(x), buf2)
        return buf2
    
    def repr(self):
        left = self._repr_left()
        top = self._repr_top()
        field = self._repr_field()
        middle = " "*len(left[0])+"+"+"-"*len(field[0])
        top = map(lambda x:" "*(len(left[0])+1)+x, top)
        bottom = zip(left, field)
        bottom = map(lambda x:"|".join(x), bottom)
        return "\n".join(top)+"\n"+middle+"\n"+"\n".join(bottom)
        
class PosIter(object):
    def __init__(self, nitem, total):
        self._nitem = nitem
        self._total = total
        self._ar = []
    
    def next(self):
        if self._ar == []:
            self._ar = [0]*self._nitem
            return self._ar
        if sum(self._ar) < self._total:
            self._ar[0] += 1
            return self._ar
        # sum == total
        if self._is_last():
            return None
        idx = self._mostleft()
        self._ar[idx] = 0
        self._ar[idx+1] += 1
        return self._ar
    
    def _is_last(self):
        if sum(self._ar) < self._total:
            return False
        for i in range(len(self._ar)):
            if self._ar[i] != 0 and i < len(self._ar)-1:
                return False
        return True
    
    def _mostleft(self):
        for i in range(len(self._ar)):
            if self._ar[i] != 0:
                return i
        return i
    
class LineMaker(object):  
    def __init__(self, profile, width):
        self._profile = profile
        self._width = width
        self._pos = PosIter(len(self._profile), self._postotal())
        
    def next(self):
        pos = self._pos.next()
        if not pos:
            return None
        return self._pos2line(pos)
        
    def _postotal(self):
        '''calculate PosIter total'''
        return self._width - sum(self._profile) - len(self._profile) + 1
    
    def _pos2line(self, pos):
        p = pos[:]
        p.append(self._postotal()-sum(p))
        if len(p) > 2:
            p[1:-1] = map(lambda x: x+1, p[1:-1])
        buf = []
        for i in range(len(self._profile)):
            buf.extend([Nonogram.WHITE]*p[i])
            buf.extend([Nonogram.BLACK]*self._profile[i])
        buf.extend([Nonogram.WHITE]*p[-1])
        return buf
    
                   
def _read_profile(csvfile):            
    profreader = csv.reader(csvfile, delimiter=' ')
    leftprof = []
    for row in profreader:
        if not row:
            break
        if row[0] != '#':
            leftprof.append(map(int, row))
    topprof = []
    for row in profreader:
        if row[0] != '#':
            topprof.append(map(int, row))
    return [leftprof, topprof]
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Nonogram solver.')
    parser.add_argument('fname', metavar='fname', type=str,
                        help='profile data file (space separated)')

    args = parser.parse_args()
    fobj = open(args.fname, 'rb')
    left, top = _read_profile(fobj)
    fobj.close()
    n = Nonogram()
    n.set_left(left)
    n.set_top(top)
    n.solve()
    print n.repr()
    
