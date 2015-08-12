# Piotr Bogun
# Merge Sort
# mergeSort('10_Random.txt') <-- Copy/Pase call

numOps = 0
numComp = 0

def mergeSort(file):
    
    # Reset globals for each run
    global numOps
    global numComp
    numOps = 0
    numComp = 0

    # Opens file and outputs into int(list(nums))
    nums = []
    infile = open(file, 'r')
    strnums = [x.strip() for x in infile.readlines()]
    infile.close
    for x in strnums:
        nums.append(int(x))

    _mergeSort(nums)
    
    print("Compares = {x}\nOperations = {y}".format(x = numComp, y = numOps))
    return nums


def _mergeSort(alist):
    # MergeSort Algorithm

    global numOps
    global numComp

    # Breaks list into smaller pieces
    if len(alist) > 1:
        numComp += 1
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        numOps += 3

        _mergeSort(lefthalf)
        _mergeSort(righthalf)

        i=0
        j=0
        k=0
        numOps += 3

        # Merges sorted pieces together
        while i < len(lefthalf) and j < len(righthalf):
            numComp += 2
            if lefthalf[i] < righthalf[j]:
                numComp += 1
                alist[k] = lefthalf[i]
                i = i+1
                numOps += 2
            else:
                alist[k] = righthalf[j]
                j = j+1
                numOps += 2
            k = k+1
            numOps += 1

        while i < len(lefthalf):
            numComp += 1
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
            numOps += 3

        while j < len(righthalf):
            numComp += 1
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
            numOps += 3
