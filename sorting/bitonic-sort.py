def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonic_merge(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonic_merge(a, low, k, dire)
        bitonic_merge(a, low + k, k, dire)

def bitonic_sort(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        bitonic_sort(a, low, k, 1)
        bitonic_sort(a, low + k, k, 0)
        bitonic_merge(a, low, cnt, dire)

A = [9,4,6,7,99]
up = 1
n = len(A)

bitonic_sort(A, 0, n, up)
print(A)
