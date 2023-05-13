import time
import random

#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))

v = []
# -------------------------------------------------BUBBLE SORT----------------------------------------------------------
def bubbleSort(lenght):
    start_time = time.time()
    for iIndex in range(lenght):
        swapped = False
        for jIndex in range(0, lenght - iIndex - 1):
            if v[jIndex] > v[jIndex + 1]:
                v[jIndex], v[jIndex + 1] = v[jIndex + 1], v[jIndex]
                swapped = True
        if swapped == False:
            break
    print("--- %s seconds ---" % (time.time() - start_time))

# -------------------------------------------------MERGE SORT-----------------------------------------------------------
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def mergerunner():
    n = len(v)
    start_time = time.time()
    mergeSort(v, 0, n - 1)
    print("--- %s seconds ---" % (time.time() - start_time))

#-------------------------------------------------INSERT SORT-----------------------------------------------------------

def insertionSort():
    start_time = time.time()
    for scanIndex in range(1, len(v)):
        tmp = v[scanIndex]

        minIndex = scanIndex

        while minIndex > 0 and tmp < v[minIndex - 1]:
            v[minIndex] = v[minIndex - 1]
            minIndex -= 1

        v[minIndex] = tmp
    print("--- %s seconds ---" % (time.time() - start_time))

#-------------------------------------------------HEAP SORT-------------------------------------------------------------

def createHeap(data, length, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and data[index] < data[left]:
        largest = left

    if right < length and data[largest] < data[right]:
        largest = right

    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        createHeap(data, length, largest)

def heapSort():
    length = len(v)
    start_time = time.time()
    #We build max heap
    for index in range(length, 0, -1):
        createHeap(v, length, index)

    for index in range(length -1, 0, -1):
        v[index], v[0] = v[0], v[index]
        createHeap(v, index, 0)

    print("--- %s seconds ---" % (time.time() - start_time))

#-------------------------------------------------BUCKET SORT-----------------------------------------------------------


def bucketSort(array):
    start_time = time.time()
    largest = max(array)
    length = len(array)
    size = largest / length

    # Create Buckets
    buckets = [[] for i in range(length)]

    # Bucket Sorting
    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    # Sorting Individual Buckets
    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])

    # Flattening the Array
    result = []
    for i in range(length):
        result = result + buckets[i]

    print("--- %s seconds ---" % (time.time() - start_time))
#-------------------------------------------------QUICK SORT------------------------------------------------------------

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

#-------------------------------------------------MAIN------------------------------------------------------------------
def main():
    print("Input x:")
    x = int(input())
    for i in range(x):
        v.append(i)
    print("How many times?")
    t = int(input())
    print("What algorithm?")
    opt = input()
    for i in range(t):
        random.shuffle(v)
        print("Test ", i+1)
        if opt == "bubble":
            bubbleSort(x)
        elif opt =="merge":
            mergerunner()
        elif opt =="heap":
            heapSort()
        elif opt == "bucket":
            bucketSort(v)
        elif opt == "insert":
            insertionSort()
        elif opt == "quick":
            start_time = time.time()
            quickSort(v, 0, x-1)
            print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()

