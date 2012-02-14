"""
    Author: James Meldrum
    Date: Mar 1, 2010
    Lang: Python 2.7
    Desc: Full linked-list implementation of the bag.

"""


class Bag(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._head = None # Reference to the first element in the lst
        self._size = 0  # Count of the number of objects in the bag.
                        # Not necessary but useful as the Bag gets
                        # bigger
                        
    def __len__(self):
        return self._size
    
    def __contains__(self,target):
        curNode = self._head # Current node for iteration.
        while curNode is not None and curNode.item != target:
            curNode = curNode.next # Investigate this
        return curNode is not None
    
    # Prepending
    def add(self,item):
        newNode = _BagListNode(item) # Init new llist item
        newNode.next = self._head # Set new node attr to current header ref
        self._head = newNode # Set local attr to ref new node
        self._size +=1 # Increment counter
        
    def remove (self,item):
        predNode = None # Init predecessor node as None.
        curNode = self._head # First element in list
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next
        assert curNode is not None, "The item must be in the bag!" # SS return.

        # Unlink the node and return the item
        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.item
    
    def __iter__(self):
        return _BagIterator(self._head)
    
class _BagListNode(object):
    def __init__(self,item):
        self.next = None
        self.item = item
        
class _BagIterator(object):

    def __init__(self,listHead):
        self._curNode = listHead
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curNode is None:
            return StopIteration
        else:
            item = self._curNode.item # Get the value to return
            self._curNode = self._curNode.next # Step pointer forward one
            return item    