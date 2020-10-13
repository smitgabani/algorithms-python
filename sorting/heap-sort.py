def maxheapify(A, n, i): 
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and A[i] < A[l]: 
        largest = l 

    if r < n and A[largest] < A[r]: 
        largest = r 

    if largest != i: 
        A[i], A[largest] = A[largest], A[i]
        maxheapify(A, n, largest) 

def heapSort(A): 
    n = len(A) 

    for i in range(n//2 - 1, -1, -1): 
        maxheapify(A, n, i) 

    for i in range(n-1, 0, -1): 
        A[i], A[0] = A[0], A[i] 
        maxheapify(A, i, 0) 

A = [16,4,10,14,7,9,3,2,8,1,99]
heapSort(A) 
print(A)
