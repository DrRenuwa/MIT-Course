def fib(n):
    
    global runTime
    runTime += 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
    
def fibv2(n, d):
       
    global runTime
    runTime += 1
    
    if n in d:
        return d[n]
    else:
        ans = fibv2(n-1, d) + fibv2(n-2, d)
        d[n] = ans
        return ans
    
    
d = {1:1, 2:2}

runTime = 0
number = 10

#print(fib(number))
print(fibv2(number, d))

print("Runtime " + str(runTime))