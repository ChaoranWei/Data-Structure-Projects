"""This module provides an implementation of time ADT.

The ADT is implemented in Time class.

Author: Chaoran Wei (cwei02)
"""
class Time:
    """Time ADT
        
   Time ADT is a tool to show represent the normal time with the input of 
   seconds ellipsed from the last midnight. Time can be calculated and compared
   with other time, and is represented as a 12-hour clock.
    """    
    def __init__(self, hours, minutes, seconds):
        """Construct a time class as the seconds passed since midnight.
        
        Arguments:
        sumsec -- An integer that represents the seconds passed since midnight.
        """
        assert 0 <= seconds <= 59, 'Seconds input should be in the range. '
        assert 0 <= minutes <= 59, 'Minutes input should be in the range. '
        assert 0 <= hours <= 23, 'Hours input should be in the range. '
        self._sumsec = hours * 3600 +  minutes * 60 + seconds
        
    def hour(self):
        """Return the hour of the time. """
        return (self._timetuple())[0]
    
    def minute(self):
        """Return the minute of the time. """
        return (self._timetuple())[1]
    
    def second(self):
        """Return the second of the time. """
        return (self._timetuple())[2]
    
    def numSeconds(self, otherTime):
        """Calculates the total seconds between the time and the other time.
        
        Arguments:
        otherTime -- the other time
        """
        difference = abs(self._sumsec - otherTime._sumsec)
        return difference
    
    def isAM(self):
        """Determine if the time is in the morning(AM). """
        hour, minute, second = self._timetuple()
        return 0 <= hour <= 11
        
    def isPM(self):
        """Determine if the time is in the afternoon(PM). """
        hour, minute, second = self._timetuple()
        return 12 <= hour <= 23
        
    def __eq__(self, otherTime):
        """Compare the time with the other time if they are equal.
        
        Arguments:
        otherTime -- the other time
        """
        return self._sumsec == otherTime._sumsec
    
    def __lt__(self, otherTime):
        """Compare the time with the other time if one is less than the other.
                
        Arguments:
        otherTime -- the other time
        """        
        return self._sumsec < otherTime._sumsec
    
    def __le__(self, otherTime):
        """Compare the time with the other time if one is less than or equal 
        to the other.
                
        Arguments:
        otherTime -- the other time
        """                
        return self._sumsec <= otherTime._sumsec
    
    def __ne__(self, otherTime):
        """Compare the time with the other time if they are not equal.
            
        Arguments:
        otherTime -- the other time
        """
        return self._sumsec != otherTime._sumsec
        
    def __str__(self):
        """Return the time as a string. """
        hour, minute, second = self._timetuple()
        if hour > 12:
            hour = hour - 12
            return '%02d:%02d:%02d PM' % (hour, minute, second)
        elif hour == 12:
            return '%02d:%02d:%02d PM' % (hour, minute, second)
        else:
            return '%02d:%02d:%02d AM' % (hour, minute, second)
        
        
    def _timetuple(self):
        """Return the time as a tuple. """
        hours = int(self._sumsec / 3600)
        minutes = int((self._sumsec - hours * 3600) / 60)
        seconds = int(self._sumsec - hours * 3600 - minutes * 60 )
        
        return hours, minutes, seconds
    

