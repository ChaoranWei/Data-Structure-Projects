'''This module provides an implementation of HashMap ADT.

The ADT is implemented in HashMap class.

Author: Chaoran Wei
'''
from arrayadt import Array
class _MapEntry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value  
        
class HashMap :
    '''HashMap ADT
    HashMap ADT is the implementation of map data structure using hash table.
    '''
    UNUSED = None
    EMPTY = _MapEntry( None, None )        

    def __init__( self ):
        '''Constructs an empty map using array. '''
        self._table = Array( 7 )
        self._count = 0
        self._maxCount = len(self._table) - len(self._table) // 3   

    def __len__( self ):
        '''Returns the length of the map. '''
        return self._count

    def __contains__( self, key ):
        '''Determines if a key in contained in the hash map. 
        
        Arguments:
        key -- The key we want to search the membership
        '''
        slot = self._findSlot( key, False )
        return slot is not None

    def add( self, key, value ):
        '''Adds a new key value pair into the map.
        
        Arguments:
        key -- the key of the added pair
        value -- the value of the added pair
        '''
        if key in self :
            slot = self._findSlot( key, False )
            self._table[slot].value = value
            return False
        else :
            slot = self._findSlot( key, True )
            self._table[slot] = _MapEntry( key, value )
            self._count += 1
            if self._count == self._maxCount :
                self._rehash()
            return True

    def valueOf( self, key ):
        '''Returns the value of corresponding key.
        
        Arguments:
        key -- the key of the value to be searched
        '''
        slot = self._findSlot( key, False )
        assert slot is not None, "Invalid map key."
        return self._table[slot].value

    def remove( self, key ):
        '''Removes the key in the hash map.
        
        Arguments:
        key -- the key of the pair to be removed
        '''
        slot = self._findSlot( key, False )
        if slot is not None:
            self._table[slot] = HashMap.EMPTY
            self._count -= 1

    def __iter__( self ):
        '''The iteration function which passes to the hidden iterator class.
        '''
        return _HashIterator( self._table)
 
    def _findSlot( self, key, forInsert ):
        slot = self._hash1( key )
  
        M = len(self._table)
        while self._table[slot] is not HashMap.UNUSED:
            if forInsert and self._table[slot] is HashMap.EMPTY :
                return slot
            elif not forInsert and \
                 (self._table[slot] is not HashMap.EMPTY and self._table[slot].key == key) :
                return slot
            else :
                slot = (slot + 1) % M
        
        if forInsert:
            return slot
        else:
            return None
 
    def _rehash( self ) :
  
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array( newSize )
        
        self._count = 0
        self._maxCount = newSize - newSize // 3
  
        for entry in origTable :
            if entry is not HashMap.UNUSED and entry is not HashMap.EMPTY :
                slot = self._findSlot( entry.key, True )
                self._table[slot] = entry
                self._count += 1

    def _hash1( self, key ):
        return abs( hash(key) ) % len(self._table)
 

class _HashIterator :
  
    def __init__( self, theTable ):
        self._HashRef = theTable
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        while self._curNdx < len( self._HashRef ) and (self._HashRef[ self._curNdx ] \
        is HashMap.UNUSED or self._HashRef[ self._curNdx ] is HashMap.EMPTY):
            self._curNdx += 1
    
        if self._curNdx == len( self._HashRef ):
            raise StopIteration  
        else:
            entry = self._HashRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        
        