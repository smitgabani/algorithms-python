def hoare_par(A, p, r):
    
    x = A[p]
    i = p - 1
    j = r + 1
    
    while True:
        j -= 1
        while (A[j] > x):
            j -= 1
            
        i += 1
        while (A[i] < x):
            i += 1
            
        if (i >= j):
            return j
        
        A[i], A[j] = A[j], A[i]

def quickSort(A, p, r):
    if p < r:
        q = hoare_par(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

A = [9,8,7,6,5,4,3,2,1]
n = len(A)
quickSort(A, 0, n-1)
print(A)
