'''
Created on 2014/09/17

@author: alchu
'''

from nonogram import Nonogram

if __name__ == '__main__':
    n = Nonogram()
    n.set_left([[2],[1],[1]])
    n.set_top([[2],[1,1]])
    n.solve()
    print n.repr()
    