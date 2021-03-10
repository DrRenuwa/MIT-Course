def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    for i in range(a, 0, -1):
        if a%i == 0 and b%i == 0:
            return i
            break
        
print(gcdIter(210,180))

