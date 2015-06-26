class _GListNode:  
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class GList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._cur = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def __contains__(self, item):
        self._cur = self._head
        for i in range(self._size):
            if item == self._cur.data:
                return True
            self._cur = self._cur.next
        return False
        
        
    def clear(self):
        self._head = None
        self._tail = None
        self._cur = None
        self._size = 0        
    
    def append(self,item): 
        newNode = _GListNode(item)
        if self._head == None:
            self._head = newNode
        else:
            newNode.prev = self._tail
            self._tail.next = newNode
        self._tail = newNode
        self._cur = newNode
        self._size += 1
    
    def findNext(self):
        assert self._cur is not None, 'Current Node not found. '
        if self._cur.next is not None:
            self._cur = self._cur.next
            return True
        else:
            return False
    
    def findPrevious(self):
        assert self._cur is not None, 'Current Node not found. '
        if self._cur.prev is not None:
            self._cur = self._cur.prev
            return True
        else:
            return False
        
    def get(self):
        if self._cur is not None:
            return self._cur.data
    
    def getFirst(self):
        if self._head is not None:
            self._cur = self._head
            return self._head.data
            
    def getLast(self):
        if self._tail is not None:
            self._cur = self._tail
            return self._tail.data        
        
    def getNext(self):
        assert self._cur is not None, 'Current Node not found. '
        if self._cur.next is not None:
            self._cur = self._cur.next
            return self._cur.data
        else:
            self._cur = None
    
    def getPrevious(self):
        assert self._cur is not None, 'Current Node not found. '
        if self._cur.prev is not None:
            self._cur = self._cur.prev 
            return self._cur.data
        else:
            self._cur = None
    
    def prepend(self, item):
        newNode = _GListNode(item)
        if self._head == None:
            newNode.data = item
            self._tail = newNode
        else:
            newNode.next = self._head
            self._head.prev = newNode
        self._head = newNode
        self._cur = newNode
        self._size += 1
        
    def insert(self, item):
        assert self._cur is not None, 'Current Node not found. '
        newNode = _GListNode(item)
        if self._cur == self._head:
            self.prepend(item)
        else:
            newNode.next = self._cur
            self._cur.prev.next = newNode
            newNode.prev = self._cur.prev
            self._cur.prev = newNode
            self._cur = self._cur.prev
            self._size += 1
       
    def remove(self): 
        assert self._cur is not None, 'Current Node not found. '
        self._size -= 1
        if self._head == self._tail:
            self.clear()
        elif self._cur is self._tail:
            self._cur = self._cur.prev
            self._tail = self._cur
            self._tail.next = None
        elif self._cur is self._head:
            self._cur = self._cur.next
            self._head = self._cur
            self._head.prev = None
        else:
            self._cur = self._cur.prev
            self._cur.next = self._cur.next.next
            
            
    