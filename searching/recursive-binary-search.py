def rbsearch(A, v, low, high):
	if high >= low :
		mid = low + (high - low) // 2

		if A[mid] == v:
			return mid

		elif A[mid] > v:
			return rbsearch(A, v, low, mid-1)

		else:
			return rbsearch(A, v, mid+1, high)

	else:
		return -1

A = [1,2,3,4,5,6,7,8,9,0]
print(A)
v = int(input("Enter Key: "))
index = rbsearch(A, v, 0, len(A))

if index == -1:
	print("Key not present in the array")
else:
	print("\nKey present at index",index,"position",index+1 )
