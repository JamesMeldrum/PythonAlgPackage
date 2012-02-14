'''
Author: James Meldrum (Team Delta)
Date: Feb 6, 2010
Lang: Python 2.7
Desc: Hardware-supported Binary Hash Map
'''

class BSTMap(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._root = None
        self._size = 0
        
    def __contains__(self,key):
        return self._bstSearch(self._root,key) is not None
        
    def __len__(self):
        return self._size
    
    def __iter__(self):
        return _BSTMapIterator(self._root)
    
    def add(self,key,value):
        node = self._bstSearch(key)
        
        if node is not None:
            node.value = value # Overwrite the value
            return False
        else:
            self._root = self._bstInsert(self._root,key,value)
            self._size +=1
            return True
        
    def _bstInsert(self,subtree,key,value):
        if subtree is None:
            subtree = self._BSTMapNode(key,value)
        elif key < subtree.key:
            subtree.left = self._bstInsert(subtree.left,key,value)
        elif key > subtree.key:
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree
    
    def valueOf(self,key):
        node = self._bstSearch(self._root,key)
        assert node is not None, "Invalid map key"
        return node.value
    
    def _bstSearch(self,subtree,target):
        if subtree is None: # Not found
            return None # Base case
        elif target < subtree.key:
            return self._bstSearch(subtree.left,target)
        elif target > subtree.key:
            return self._bstSearch(subtree.right,target)
        else:
            return subtree # Value is found. Key == Target
    
    def _bstMinimum(self,subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum(subtree.left)
    
class BSTMapNode(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
class _BSTMapIterator(object):
    
    def __init__(self):
        pass