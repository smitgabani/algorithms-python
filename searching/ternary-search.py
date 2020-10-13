def tersearch(A, v, low, high):
	if (high >= low):

		mid1 = low + (high - low) // 3
		mid2 = mid1 + (high - low) // 3

		if A[mid1] == v:
			return mid1

		if A[mid2] == v:
			return mid2

		if A[mid1] > v:
			return tersearch(A, v, low, mid1-1)

		if A[mid2] < v:
			return tersearch(A, v, mid2+1, high)

		return tersearch(A, v, mid1+1, mid2-1)
	return -1

arr = [ 10, 12, 13, 16, 18, 19, 20,
        21, 22, 23, 24, 33, 35, 42, 47 ]
v = int(input("Enter key: "))
n = len(arr)
match = tersearch(arr, v, 0, n-1)

if match == -1:
	print("\nKey not present in the array")
else:
	print("\nKey present at index",match,"position",match+1 )
