'''
Author: James Meldrum (Team Delta)
Date: Feb 6, 2010
Lang: Python 2.7
Desc: Hardware-supported array ADT using ctypes
'''

import ctypes

class Array(object):
    '''
    classdocs
    '''

    def __init__(self,size):
        '''
        Constructor
        '''
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size # Init c array
        self._elements = PyArrayType() # Get local handle
        self.clear(None)
        
    def __len__(self):
        return self._size
    
    def __getitem__ (self,index):
        assert index >= 0 and index < len(self), "Arrat subscript out of range"
        return self._elements[index]

    def __setitem__(self,index,value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value
    
    def clear(self,value):
        for i in range(len(self)):
            self._elements[i] = value
            
    def __iter__(self):
        return _ArrayIterator (self._elements)
    
    
class _ArrayIterator(object):
    
    def __init__(self,theArray):
        self._arrayRef = theArray
        self._curNdx = 0
        
    def __iter__(self):
        return self
      
    def __next__ (self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
    