def shsort(A):
    n = len(A)
    g = n // 2
    while g > 0:
        for x in range(g, n):
            y = A[x]
            z = x
            while z >= g and A[z - g] > y:
                A[z] = A[z - g]
                z -= g
            A[z] = y
        g //= 2

mylist = input('Enter the list values to be stored: ').split()
shsort(mylist)
print(mylist)
