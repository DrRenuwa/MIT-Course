def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    
    if char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[0:len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2:])
     
print(isIn('g', 'bcqqu'))