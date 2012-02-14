"""
    Author: James Meldrum
    Date: Feb 22, 2010
    Lang: Python 2.7
    Desc: Optimised list for Django shopping cart application. Uses linked-list ahead of standard list implementation 

"""

class Bag(object):
    '''
    classdocs
    '''

    # Constructor
    def __init__(self):
        self._theItems = list()
        
    # Returns the number of items in the bag
    def __len__(self):
        return len(self.theItems)

    # Determines if an item is in the bag
    def __contains__(self,item):
        return item in self._theItems
    
    # Adds a new item to the bag
    def add(self,item):
        self._theItems.append(item)
        
    # Removes and returns an instance of the item from the bag
    def remove(self,item):
        assert item in self._theItems, "The item must be in the bag"
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)
    
    # Returns an iterator for traversing the list of items
    def __iter__(self):
        return _BagIterator(self._theItems)
    

class _BagIterator:

    """
        Iteration helper class for Bag
        Example usage.
        
        for item in bag:
            print(item)
            
            1) Call to Bag.__iter__
            2) _BagIterator construction
            3) Repeat the while loop until a break is called
    """

    def __init__(self, theList):
        self._bagItems = theList
        self.curItem = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration