""" This module provides two implementations of fibonacci sequence operations.

The evaluation of time elipse and verification are included.

Author: Chaoran Wei
"""

import time

def main():
    """ This main function execute the whole fibonacci sequence evaluation
    code. Then it compares the time elipse of recursive and non-recursive 
    method and draw verification histogram. 
    """
    n = int(input("Enter n: "))
    print()
    
    t0 = time.time()
    f1 = fib1(n)
    print("fib1(%d) = %d" % (n, f1))
    t1 = time.time()
    print("fib1 elapsed time is %5.3f." % (t1-t0))
    
    print()

    t0 = time.time()
    f2 = fib2(n)
    print("fib2(%d) = %d" % (n, f2))
    t1 = time.time()
    print("fib2 elapsed time is %5.3f." % (t1-t0))
    
    print()

    if f1 != f2:
        print("Test failed!")

    print()
    
    printFibHistogram(10)

def fib1(n):
    """ This function returns the n_th fibonacci sequence using iterative
    method.
    
    Arguments:
    n -- n_th sequence
    """
    assert n >= 0, "Fibonacci not defined for n < 0."
    n0 = 0
    n1 = 1
    for i in range(n-1):
        n = n0 + n1
        n0 = n1
        n1 = n
    return n

def fib2(n):
    """ This function returns the n_th fibonacci sequence using recursive
    method.
    
    Arguments:
    n -- n_th sequence
    """
    if n == 0 or n == 1 :
        return n
    else :
        return fib2(n - 1) + fib2(n - 2) #This part directly cites the note


def printFibHistogram(n):
    """ This function print the histogram for fib1 and fib2 function and 
    compare the two. """
    
    for i in range(n):
        print('*' * fib1(i+1))
   	 
    print("\nCheck the above and below histogram to see if they are identical")
    print("Otherwise, something is wrong!\n")

    for i in range(n):
        print('*' * fib2(i+1))

main()