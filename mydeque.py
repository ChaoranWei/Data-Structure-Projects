'''This Model provides the implementation of deque ADT.

The ADT is implemented in MyDeque class.

Author:Chaoran Wei (cwei02)
'''
class MyDeque:
    '''MyDeque ADT
    
    MyDeque ADT is a type of queue which allows to add and remove items 
    at both ends.
    '''
    def __init__(self):
        '''Constructs an empty deque using python list. '''
        self._qlist = list()
        
    def isEmpty(self):
        '''Checks if the deque is empty. '''
        return len(self) == 0
    
    def __len__(self):
        '''Returns the length of the deque. '''
        return len(self._qlist)
    
    def addFirst(self, item):
        '''Inserts the specified item at the front of the deque. 
        
        Arguments:
        item -- the item to be inserted.
        '''
        self._qlist.insert(0, item)
        
    def addLast(self, item):
        '''Adds the specified item at the back of the deque.
        
        Arguments:
        item -- the item to be added.
        '''
        self._qlist.append(item)
    
    def removeFirst(self):
        '''Removes and returns the first item of this deque. '''
        assert len(self) != 0, 'Cannot remove empty deque. '
        item = self._qlist.pop(0)
        return item
    
    def removeLast(self):
        '''Removes and returns the last item of the deque. '''
        assert len(self) != 0, 'Cannot remove empty deque. '
        item = self._qlist.pop(len(self) - 1)
        return item
    
    def peekFirst(self):
        '''Returns but does not remove the first item of the deque. '''
        if a.isEmpty() is True:
            return None
        else:  
            return self._qlist[0]
    
    def peekLast(self):
        '''Returns but does not remove the last item of the deque. '''
        if a.isEmpty() is True:
            return None
        else:         
            return self._qlist[len(self) - 1]
        