"""
    Author: James Meldrum
    Date: Feb 13, 2010
    Lang: Python 2.7
    Desc: Implementation of Hash Map 

"""


class Map(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.entryList = list()
        
    def __len(self):
        return len(self.entryList)
    
    def __contains__(self,key):
        ndx = self._findPosition(key)
        return ndx is not None
    
    def add(self,key,value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self.entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key,value)
            self.entryList.append(entry)
            return True
        
    def valueOf(self,key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid Map Key"
        return self._entryList[ndx].value 

    def remove(self,key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid Map Key"
        self.entryList.pop(ndx)
        
    def __iter__(self):
        return _MapIterator(self.entryList)

    def _findPosition(self,key):
        for i in range(len(self)):
            if self.entryList[i].key == key:
                return i
        return None

class _MapEntry(object):
    def __init__(self,key,value):
        self.value = value
        self.key = key
    
class _MapIterator(object):

    def __init__(self,entryList):
        self._entryListRef = entryList
        self._curNdx = 0
    
    def __next__(self):
        if self._curNdx < len(self._entryListRef):
            entry = self._entryListRef[self._curNdx]
            self._curNdx +=1
            return entry
        else:
            raise StopIteration