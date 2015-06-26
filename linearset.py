"""This module provides an implementation of Set ADT.

The ADT is implemented in Set class.

Author: Chaoran Wei(cwei02)
"""
class Set :
    """Set ADT
    Set ADT is a data structure to collect elements and evaluate the 
    interaction among different sets.
    """
    def __init__( self ):
        '''Constructs an empty set. '''
        self._theElements = list()
        
    def __len__( self ):
        '''Returns the number of items in the set. '''
        return len( self._theElements )
    
    def __contains__( self, element ):
        """ Determines if an element is contained in the set.
                
        Arguments:
        element -- the element to be checked if contained in the set
        """
        return element in self._theElements
    
    def add( self, element ):
        """ Adds a new element to the set.
                 
        Arguments:
        element -- the element to be added into the set
        """
        if element not in self :
            self._theElements.append( element )

    def remove( self, element ):
        """ Removes and returns an instance of the element from the set.
                 
        Arguments:
        element -- the element to be removed from the set
                 
        Precondition:
                The element must be in the set
        """
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)
        
    def __eq__( self, setB ):
        '''Check if the set is equal to another set
        
        Arguments:
        setB -- the other set to compare with
        '''
        if len( self ) != len( setB ) :
            return False
        else :
            return self.isSubsetOf( setB )
        
    def isSubsetOf( self, setB ):
        '''Determine whether another set is the subset of the set
        
        Argument:
        setB -- the other set of check
        '''
        for element in self :
            if element not in setB :
                return False
        return True
 
    def union( self, setB ):
        '''Returns the union of two sets
        
        Arguments:
        setB -- another set to join the union
        '''
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for element in setB :
            if element not in self :
                newSet._theElements.append( element )
                return newSet
            
    def interset( self, setB ):
        '''Returns the intersection of two sets
                
        Arguments:
        setB -- another set to evaluate the intersection with
        '''        
        newSet = Set()
        for element in setB:
            if element in self:
                newSet._theElements.append( element )
                return newSet

    def difference( self, setB ):
        '''Returns the difference from the other set
                
        Arguments:
        setB -- another set to compare the difference with
        '''        
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for element in self.interset(setB):
            newSet.remove(element)
            return newSet
        
    def __iter__( self ):
        """Returns an iterator for traversing the list of elements in the set.
        """        
        return _SetIterator( self._theElements )
    
class _SetIterator :
    def __init__( self, theSet ):
        self._setRef = theSet
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._setRef ) :
            entry = self._setRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration