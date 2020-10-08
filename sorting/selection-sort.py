def selsort(A):
    r = len(A)
    for x in range(r):
        minimum = x
        for y in range(x + 1, r):
            if A[y] < A[minimum]:
                minimum = y
        (A[x], A[minimum]) = (A[minimum],A[x])

mylist = input('Enter the list values to be stored: ').split()
selsort(mylist)
print(mylist)
