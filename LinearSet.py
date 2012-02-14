"""
    Author: James Meldrum
    Date: Feb 12, 2010
    Lang: Python 2.7
    Desc: Implementation of mathematical set. Mainly to test out Python built-ins. Incomplete. Address iterator.

"""


class Set(object):

    def __init__(self):
        self._theElements = list()
        
    def __len__(self):
        return len(self._thElements)
    
    def __contains__(self,element):
        return element in self._theElements
    
    def add(self,element):
        if element not in self:
            self._theElements.append(element)
            
    def remove(self,element):
        assert element in self._theElements, "The element must be in the set"
        self._theElements.remove(element)
        
    def __eq__(self,setB):
        if len(self._theElements) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
        
    def isSubsetOf(self,setB):
        for element in self:
            if element not in setB:
                return False
        return True
    
    def union(self,setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet
    
    def intersect(self,setB):
    # Present in setB, not set A
        pass
    
    def difference(self,setB):
    # Present in SetA, not set B
        pass
    
    def __iter__(self):
        return _SetIterator(self._theElements)
    
class _SetIterator():
    '''
        Requires completion.
        __next__, 
    '''
    def __init__(self):
        pass