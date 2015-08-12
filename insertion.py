# Piotr Bogun
# Insertion Sort
# insertionSort('10_Random.txt')  <--- Copy/Paste call

def insertionSort(file):
    # Runs insertion sort on specified file
    
    compareCount = 0
    operationCount = 0

    # Opens file(file) and turns into list(int(nums))
    infile = open(file, 'r')
    strnums = [x.strip() for x in infile.readlines()]
    nums = []
    infile.close
    for x in strnums:
        nums.append(int(x))

    # Insertion sorting algorithm with counting of compares and operations
    for i in range(1, len(nums)):
        j = i-1
        key = nums[i]
        operationCount += 2

        while (nums[j] > key) and (j >= 0):
            nums[j+1] = nums[j]
            j -= 1
            operationCount += 2
            compareCount += 2
        nums[j+1] = key
        operationCount += 1

    print("Compares = {x}\nOperations = {y}".format(x = compareCount, y = operationCount))
    return nums
