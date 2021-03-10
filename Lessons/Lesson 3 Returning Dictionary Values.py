animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

'''
def how_many(aDict):

    for i in aDict:
        if isinstance(aDict[i], list):
            count += len(aDict[i])

    return count
'''

'''
def how_many(aDict):
    
    count = 0
    for i in aDict.values():
        count += len(i)
    
    return count


#print(how_many(animals))
'''

def biggest(aDict):
    
    biggestKey = "a"
    
    if len(aDict[max(aDict.keys())]) == 0:
        return None
    else:
        for keys in aDict.keys():
            for values in aDict[keys]:
                if len(aDict[keys]) > len(aDict[biggestKey]):
                    biggestKey = keys     
                    
        return biggestKey
        

print (biggest(animals))