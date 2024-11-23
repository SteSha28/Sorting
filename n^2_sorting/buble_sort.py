import random


def buble_sort(arr: list) -> list:
    flag = True
    while flag:
        swap = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap += 1
        if not swap:
            flag = False
    return arr


arr = [random.randint(-20, 20) for _ in range(20)]
print(*arr)
print(*buble_sort(arr))
