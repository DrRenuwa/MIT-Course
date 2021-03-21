def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''    
    print(str(a) + " " + str(b))
    
    if b%a == 0:
        return a
    else:
        return gcdRecur(b, a%b)
        
                        
print(gcdRecur(27,3))