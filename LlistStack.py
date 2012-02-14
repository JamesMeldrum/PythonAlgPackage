"""
    Author: James Meldrum
    Date: Feb 12, 2010
    Lang: Python 2.7
    Desc: Implementation of Stack in Python 

"""

class Stack(object):
    
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self,item):
        self._top = _StackNode(item, self._top)
        self._size += 1
        
    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peak at an empty stack"
        return self._top.item # Passes value, not reference.
    
    def pop(self):
        assert not self.isEmpty(), "Cannot pop an empty stack"
        node = self._top
        self._top = self._top.next
        self._size -=1
        return node.item
    
        
class _StackNode(object):
    def __init__(self,item,top_ref):
        self._next = top_ref
        self._item = item
