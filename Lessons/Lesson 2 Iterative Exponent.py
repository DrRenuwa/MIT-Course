def iterPower(base, exp):

    ans = base
    
    while exp > 1:
        if base < 0 and exp%2 == 0:
            ans *= base
            exp -= 1
            base = -base
        else:
            ans *= base
            exp -= 1
        
    if exp == 0:
        ans = 1
        
    return ans

        
print(iterPower(-4, 0))


'''
def iterPower(base, exp):
    ans = base
    
    for i in range(1, exp):
        
        ans *= base    
        
        if exp%2 == 1:
            ans = -ans
  
    if exp == 0:
        ans = 1
    
    return ans
        
print(iterPower(-4, 2))
'''