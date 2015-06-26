"""This module provides an implementation of counter ADT.

The ADT is implemented in Counter class.

Author: Chaoran Wei (cwei02)
"""
class Counter():
    """The counter ADT
    
    A counter is a tool served as counting numbers as positive integers.
    """
    def __init__(self):
        """Construct a count as zero."""
        self._count = 0
        
    def push(self):
        """Add the count by 1. """
        self._count += 1
        return self._count
    
    def down(self):
        """minus count by 1. """
        if self._count > 0:
            self._count -= 1
            return self._count
    
    def get(self):
        """Get the current count number. """
        return self._count
        
    def reset(self):
        """Reset the counter to zero. """
        self._count = 0
        return self._count
        
    
    