# recursive interpolation search
def rintpolsearch(A, v, low, high):
	if (low <= high and v>= A[low] and v<= A[high]):

		pos = low + ((high - low ) //
			(A[high] - A[low])*(v - A[low]))

		if A[pos] == v:
			return pos

		elif A[pos] < v:
			return rintpolsearch(A, v, pos+1, high)

		elif A[pos] > v:
			return rintpolsearch(A, v, low, pos-1)
	return -1

arr = [ 10, 12, 13, 16, 18, 19, 20,
        21, 22, 23, 24, 33, 35, 42, 47 ]
print(arr)
v = int(input("Enter key: "))
n = len(arr)
index = rintpolsearch(arr, v, 0, n-1)

if index != -1:
	print("Element found at index", index)
else:
	print("Element not found")
