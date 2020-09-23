def lsearch(A,v):
    for i in range(0,n):
        if A[i] == v :
            return i
    return -1

A = [1,2,3,4,5,6,7,8,9,0]
print(A)
v = int(input("Enter Key: "))
n = len(A)

match = lsearch(A, v)

if match == -1:
    print("\nKey not present in the array")
else:
    print("\nKey present at index",match,"position",match+1 )
