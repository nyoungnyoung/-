def partition(l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def quicksort(l, r):
    if l < r:
        s = partition(l, r)
        quicksort(1, s-1)
        quicksort(s+1, r)


A = [7, 2, 5, 3, 4, 5]
N = len(A)
quicksort(0, N-1)
print(A)
