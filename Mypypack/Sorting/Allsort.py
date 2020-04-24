

def bubblesort(arr):
	n=len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
			yield arr

def insertionsort(arr):
    for i in range(1, len(arr)):
        curval = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > curval:
            arr[pos] = arr[pos - 1]
            pos -= 1
            yield arr
        arr[pos] = curval
        yield arr

def selectionsort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
        yield l


# MERGE SORT
def mergesort(arr):
    n = len(arr) - 1
    c = 1
    start = 0
    end = 0
    while c <= n:
        while end < n:
            mid = start + c // 2
            end = start + c
            if (start < n) and (end <= n):
                yield from merge(arr, start, mid, end)
                start = end + 1
            else:
                yield from merge(arr, start - c - 1, start - 1, n)
        c = 2 * c + 1
        start = 0
        end = 0


# Merge Function
def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1
        yield a
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
        yield a
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
        yield a

# HEAP SORT
def heapsort(l):
    n = len(l)
    yield from buildMaxHeap(l, n)
    for i in range(n - 1, 0, -1):
        l[0], l[i] = l[i], l[0]
        yield l
        j, index = 0, 0
        while True:
            index = 2 * j + 1
            if (index < (i - 1) and
                    l[index] < l[index + 1]):
                index += 1
            if index < i and l[j] < l[index]:
                l[j], l[index] = l[index], l[j]
                yield l
            j = index
            if index >= i:
                break


# Build Heap
def buildMaxHeap(l, n):
    for i in range(n):
        if l[i] > l[int((i - 1) / 2)]:
            j = i
            while l[j] > l[int((j - 1) / 2)]:
                (l[j],
                 l[int((j - 1) / 2)]) = (l[int((j - 1) / 2)],
                                         l[j])
                j = int((j - 1) / 2)
                yield l

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
            yield arr
  
    arr[i+1],arr[high] = arr[high],arr[i+1]
    yield arr
    return ( i+1 )
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort

def quicksort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi=yield from partition(arr,low,high)
        
        # Separately sort elements before 
        # partition and after partition 
        yield from quicksort(arr, low, pi-1) 
        yield from quicksort(arr, pi+1, high)
def quicksort1(value):
	yield from quicksort(value,0,len(value)-1)