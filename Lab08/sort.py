def bubbleSort(n):
    for i in range(len(n) - 1, -1, -1):
        for j in range(i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]


def selectionSort(n):
    for last in range(len(n) - 1, -1, -1):  # from last in list
        biggest = n[0]
        biggest_i = 0
        for i in range(1, last + 1):
            if n[i] > biggest:
                biggest = n[i]
                biggest_i = i
        n[last], n[biggest_i] = n[biggest_i], n[last]


def insertionsort(n):
    for i in range(1, len(n)):
        iEle = n[i]
        for j in range(i, -1, -1):
            if iEle < n[j - 1] and j > 0:
                n[j] = n[j - 1]
            else:
                n[j] = iEle
                break


def mergeSort(a, left, right):  # recursive sort
    if left < right:
        center = (left + right - 1) // 2
        mergeSort(a, left, center)
        mergeSort(a, center + 1, right)
        merge(a, left, center, right)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


l = [2, 4, 5, 6, 3, 1]
bubbleSort(l)
l2 = [2, 4, 5, 6, 3, 1]
selectionSort(l2)
l3 = [2, 4, 5, 6, 3, 1]
insertionsort(l3)
l4 = [2, 4, 5, 6, 3, 1]
mergeSort(l4, 0, len(l4) - 1)
print(l)
print(l2)
print(l3)
print(l4)
