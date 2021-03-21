import random

def is_sorted(L):
    for i in range(0, len(L)-1):
        if(L[i] > L[i+1]):
            return False
    return True

def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def sel_sort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

test = [8, 4, 1, 6, 5, 9, 2, 0]
# correct result [0, 1, 2, 4, 5, 6, 8, 9]


print(merge_sort(test))
