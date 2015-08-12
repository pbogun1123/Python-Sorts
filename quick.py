# Piotr Bogun
# Quick Sort
# quickSort('10_Random.txt')  <--- Copy/Paste call

# Pivot in partitions has random element, thus the number
# of compares and operations can/does vary slightly each run

import random

numOps = 0
numComp = 0

def quickSort(file):

    # Reset globals for each run
    global numOps
    global numComp
    numOps = 0
    numComp = 0

    # Opens file and outputs into int(list(nums))
    infile = open(file, 'r')
    strnums = [x.strip() for x in infile.readlines()]
    nums = []
    infile.close
    for x in strnums:
        nums.append(int(x))

    _quicksort(nums, 0, len(nums)-1)

    print("Compares = {x}\nOperations = {y}".format(x = numComp, y = numOps))
    return nums

def _quicksort( aList, first, last ):

    global numOps
    global numComp
    
    if first < last:
        numComp += 1
        pivot = partition( aList, first, last )
        _quicksort( aList, first, pivot - 1 )
        _quicksort( aList, pivot + 1, last )
 
 
def partition( aList, first, last ) :
    
    global numOps
    global numComp
    
    pivot = first + random.randrange( last - first + 1 )
    numOps += 1
    swap( aList, pivot, last )
    for i in range( first, last ):
        if aList[i] <= aList[last]:
            numComp += 1
            swap( aList, i, first )
            first += 1
            numOps += 1
 
    swap( aList, first, last )
    return first
 
 
def swap( A, x, y ):
    
    global numOps
    global numComp
    
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
    numOps += 3
