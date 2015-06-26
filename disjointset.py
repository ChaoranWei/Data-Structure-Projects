"""This module provides an implementation of Disjointset ADT.

The ADT is implemented in Disjointset class.

Author: Chaoran Wei(cwei02)
"""
from linearset import Set
class Disjointset:
    """Disjointset ADT
    Disjointset ADT is a data structure to collect sets and operate upon
    the different sets in the disjoint set
    """    
    def __init__(self):
        '''Constructs an empty disjoint set. '''
        self._disjointset = Set()
        self._len = 0
        
    def __len__(self):
        '''Returns the number of items in the disjoint set. '''
        return self._len
    
    def __contains__(self, element):
        """ Determines if an element is contained in the disjoint set.
                        
        Arguments:
        element -- the element to be checked if contained in the set
        """        
        for i in self._disjointset:
            if element in i:
                return True
        return False
    
    def add(self, element):
        """ Adds a new element to the disjoint set.
                         
        Arguments:
        element -- the element to be added into the set (as a set)
        """        
        assert element not in self, 'Element already in the set. '
        newSet = Set()
        newSet.add(element)
        self._disjointset.add(newSet)
        self._len += 1
        
    def remove(self, element):
        """ Removes and returns an instance of the element from the set.
                         
        Arguments:
        element -- the element to be removed from the set
                         
        Precondition:
            The element must be in the set
        """    
        assert element in self, 'The element not in disjoint set. '
        for i in self._disjointset:
            if element in i:
                i.remove(element)
                self._len -= 1
            if len(i) == 0:
                self._disjointset.remove(i)
            
    def union(self, element1, element2):
        '''Union two elements into one set
                
        Arguments:
        element1 -- first element to join the union
        element2 -- first element to join the union
        '''        
        assert element1 in self, 'Element1 not found.'
        assert element1 in self, 'Element2 not found.'
        for i in self._disjointset:
            if element1 in i:
                set1 = i
            elif element2 in i:
                set2 = i
                
        newSet = set1.union(set2)
        self._disjointset.add(newSet)
        self._disjointset.remove(set1)
        self._disjointset.remove(set2)
        
    def subset(self, element):
        '''Return the subset in the disjoint set that contains the element.
        
        Arguments:
        element -- The element to evaluate
        '''
        assert element in self, 'Element not found.'
        for i in self._disjointset:
            if element in i:
                return i
                    
                