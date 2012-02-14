"""
    Author: James Meldrum
    Date: Feb 8, 2010
    Lang: Python 2.7
    Desc: Partial implementation of Hash Mapping, see BSTMap for updatedsolution 

"""

from Array import Array

class HashMap(object):
    '''
    classdocs
    '''
    
    # Constants to define the status of each table entry
    UNUSED = None
    EMPTY = _MapEntry(None,None)

    def __init__(self):
        '''
        Constructor
        '''
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - len(self._table) //3 # 2/3rds rule of thumb to improve performance
        
    def __len__(self):
        return self._count
    
    def __contains__(self,key):
        slot = self._findSlot(key,False)
        return slot is not None
        
class _MapEntry(object):
    pass