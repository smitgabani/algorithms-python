def shsort(myarray, n):
    g = n // 2
    while g > 0:
        for x in range(g, n):
            y = myarray[x]
            z = x
            while z >= g and myarray[z - g] > y:
                myarray[z] = myarray[z - g]
                z -= g
            myarray[z] = y
        g //= 2
mylist = input('Enter the list values to be stored: ').split()
length = len(mylist)
shsort(mylist, length)
print(mylist)
