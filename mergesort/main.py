data = list(map(int, input().split()))


def merge(arr, left, middle, right):
    temp1 = list('0' * (middle - left + 1))
    temp2 = list('0' * (right - middle))
    for i in range(0, len(arr)):
        if i <= middle:
            temp1[i] = arr[i]
        else:
            temp2[i] = arr[i]
    i, j = 0, 0
    for k in range(0, len(arr)):
        if temp1[i] <= temp2[i]:
            arr[k] = temp1[i]
            i += 1
        else:
            arr[k] = temp2[j]
            j += 1


def mergesort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        mergesort(arr, left, middle)
        mergesort(arr, middle + 1, right)
        merge(arr, left, middle, right)


print(mergesort(data, 0, len(data)-1))