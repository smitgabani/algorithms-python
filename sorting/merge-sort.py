def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        # Recursive call on each half
        mergeSort(L)
        mergeSort(R)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
              # The value from the L half has been used
              A[k] = L[i]
              # Move the iterator forward
              i += 1
            else:
                A[k] = R[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k]=R[j]
            j += 1
            k += 1

A = input('Enter the list values to be stored: ').split()
mergeSort(A)
print(A)
