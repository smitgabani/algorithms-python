import math
def jumpsearch(A, v, n):
	step = math.sqrt(n)
	prev = 0

	while A[int(min(step, n)-1)] < v:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1
  #linear search
	while A[int(prev)]< v:
		prev += 1
		if prev == min(step, n):
			return -1
	if A[int(prev)] == v:
		return prev
array = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
print(array)
n = len(array)
v = int(input("Enter key: "))

index = jumpsearch(array, v, n)
print("Number" , v, "is at index" ,"%.0f"%index)
