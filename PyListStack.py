"""
    Author: James Meldrum
    Date: Feb 12, 2010
    Lang: Python 2.7
    Desc: Implementation of the Stack as a llist 

"""


class Stack(object):
    
    def __init__(self):
        self._items = list()
        
    def isEmpty(self):
        return len(self._items) == 0
    
    def __len__(self):
        return len(self._items)

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"      
        return self._items[-1]
        
    def pop(self):
        item_len = len(self)
        assert item_len > 0, "Stack contains no elements"
        item_val = self._items[item_len]
        self._items.pop(item_len)
        return item_val
    
    def push(self,item):
        self._items.append(item)
    