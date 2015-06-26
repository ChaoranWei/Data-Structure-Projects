""" This module provides a solution of queen board game given a size.

The 2D array data structure and private class queensBoard are provided to
faciliate the process.

Author: Chaoran Wei
"""

import ctypes

class Array :
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size

        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear( None )
    
    def __len__( self ):
        return self._size

    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value
    def __iter__( self ):
        return _ArrayIterator( self._elements )

class _ArrayIterator :
  
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration  
        
class Array2D :
    def __init__( self, numRows, numCols ):
        self._theRows = Array( numRows )
        for i in range( numRows ) :
            self._theRows[i] = Array( numCols )
    
    def numRows( self ):
        return len( self._theRows )
    
    def numCols( self ):
        return len( self._theRows[0] )
    
    def clear( self, value ):
        for row in range( self.numRows() ):
            row.clear( value )

    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
        and col >= 0 and col < self.numCols(), \
        "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]
    
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
        and col >= 0 and col < self.numCols(), \
        "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

class _QueensBoard:
    def __init__(self, n):
        n = int(n)
        self._board = Array2D(n, n)
        self._num = 0

    def size(self):
        return self._board.numRows()

    def numQueens(self):
        return self._num

    def unguarded(self, row, col):
        if self._checkRowAndCol(row, col) == True and self._checkDiag(row, col) == True:
            return True
        return False

    def placeQueen(self, row, col):
        self._board[row, col] = True 
        self._num += 1

    def removeQueen(self, row, col):
        self._board[row, col] = None
        self._num -= 1

    def reset(self):
        self._board = Array2D(self.size())

    def draw(self):
        n = self.size()
        for i in range(n):
            for j in range(n):
                if j == n-1:
                    if self._board[i, j] == True:
                        print('Q')
                    else:
                        print('_')
                else:
                    if self._board[i, j] == True:
                        print('Q', end = ' ')
                    else:
                        print('_', end = ' ')
                        
    def _checkRowAndCol(self, row, col):
        for i in range(self.size()):
            if self._board[row, i] == True:
                return False
        
            if self._board[i, col] == True:
                return False
        return True
            
    def _checkDiag(self, row, col):
        n =  self.size()
        
        for i in range(1, min(row + 1, col + 1)): #from 1 to col (row)
            if self._board[row - i, col - i] == True:
                return False
            
        for i in range(1, min(n - row, n - col)):
            if self._board[row + i, col + i] == True:
                return False
            
        for i in range(1, min(n - row, col + 1)):
            if self._board[row + i, col - i] == True:
                return False
            
        for i in range(1, min(n - col, row + 1)):
            if self._board[row - i, col + i] == True:
                return False
        return True
            
def solveNQueens(board, col ):
    '''Uses recursive method to find queen board solution. '''
    if board.numQueens() == board.size() :
        return True
    else :
        for row in range( board.size() ):
            if board.unguarded( row, col ) == True:
                board.placeQueen( row, col )
                if solveNQueens( board, col+1 ) == True:
                    return True
                else :
                    board.removeQueen( row, col )
        return False
        
def main():
    '''Executes the whole program to run the queen board solution.
    '''
    size = input('Please enter the size of the board: ')
    assert int(size) > 3, 'There will be no solution. '
    queenboard = _QueensBoard(size)
    
    solution = solveNQueens(queenboard, 0)
    if solution == True:
        queenboard.draw()
    
main()

