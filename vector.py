from arrayadt import Array

class Vector:
    def __init__(self):
        self._size = 2
        self._vector = Array(self._size)
        self._len = 0
        
    def __len__(self):
        return self._len
    
    def __contains__(self, item):
        for i in range(len(self._vector)):
            if i == item:
                return True
        return False
    
    def __getitem__(self, ndx):
        assert ndx >= 0 and ndx < self._len, "Array subscript out of range"
        return self._vector[ ndx ]
    
    def __setitem__(self, ndx, value):
        assert ndx >= 0 and ndx < self._len, "Array subscript out of range" #= or not?
        self._vector[ ndx ] = value
        
        
    def append(self, item):
        if len(self._vector) == self._len:
            self._size *= 2
            temparray = Array(self._size) #see if it works
            for i in range(len(self._vector)):
                temparray[i] = self._vector[i]
            self._vector = temparray
            
        self._vector [self._len] = item
        self._len += 1
        
    def insert(self, ndx, item):
        if len(self._vector) == self._len:
            self._size *= 2
            temparray = Array(self._size) #see if it works
            for i in range(len(self._vector)):
                temparray[i] = self._vector[i]
            self._vector = temparray     
            
        assert ndx >= 0 and ndx <= len(self), "Array subscript out of range"
        for i in range(self._len - 1, ndx - 1 ,-1):
            self._vector[i + 1] = self._vector[i]
        self._vector[ ndx ] = item
        self._len += 1
        
    def remove(self, ndx):
        for i in range(ndx + 1, len(self) + 1):
            self._vector[i - 1] = self._vector[i]
        self._vector[self._len - 1] = None
        self._len -= 1
            
    def indexOf(self, item):
        count = 0
        for i in range(len(self)):
            if self._vector[i] == item:
                return i
            count += 1
            
    def extend(self, otherVector):
        while len(otherVector) > (len(self._vector) - len(self)):
            self._size *= 2
            temparray = Array(self._size) 
            for i in range(len(self._vector)):
                temparray[i] = self._vector[i]
            self._vector = temparray      
            
        for i in range(len(otherVector)):
            self._vector[len(self) + i] = otherVector[i]
        self._len += len(otherVector)
            
    def subVector(self, From, to):
        newVector = Vector()
        for i in range(self._vector[From], self._vector[to] + 1):
            newVector.append(self._vector[i])
        
        return newVector
    
    def __iter__( self ):
            return _VectorIterator( self._elements )
        
class _VectorIterator :
  
    def __init__( self, theVector ):
        self._vectorRef = theVector
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._vectorRef ) :
            entry = self._vectorRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration  