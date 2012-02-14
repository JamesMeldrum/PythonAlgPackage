"""
    Author: James Meldrum
    Date: Nov 12, 2011
    Lang: Python 2.7
    Desc: Implementation of a matrix with less than 30% capacity for use in GMaps back-ends. Not
    as efficient as standard matrix above 30% fill.
"""

from Array import Array

class SparseMatrix(object):

    def __init__(self,numRows,numCols):
        self._numCols = numCols
        self._listOfRows = Array(numRows)
        
    def numRows(self):
        return len(self._listOfRows)
    
    def numCols(self):
        return self._numCols
    
    def __getitem__(self,ndxTuple): # returns the value of element i,j
        pass
    
    def __setitem__(self,ndxTuple,value):
        predNode = None
        row = 0
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            ## Fuck it
    