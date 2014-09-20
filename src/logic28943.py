'''
Created on 2014/09/17

@author: alchu
'''

from nonogram import Nonogram

if __name__ == '__main__':
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
    n = Nonogram()
    n.set_left(left)
    n.set_top(top)
    n.solve()
    print n.repr()