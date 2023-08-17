m = list(map(int, input().split()))
heapsize = len(m) - 1


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def heapify(m, i, heapsize):
    l = left(i)
    r = right(i)
    if (l <= heapsize) and (m[l] > m[i]):
        largest = l
    else:
        largest = i
    if (r <= heapsize) and (m[r] > m[largest]):
        largest = r
    if largest != i:
        m[i] = m[i] + m[largest]
        m[largest] = m[i] - m[largest]
        m[i] = m[i] - m[largest]
        heapify(m, largest, heapsize)


def build_heap(m, heapsize):
    for i in range(len(m)//2, -1, -1):
        heapify(m, i, heapsize)


def heapsort(m, heapsize):
    build_heap(m, heapsize)
    for i in range(len(m) - 1, 0, -1):
        m[0] = m[0] + m[i]
        m[i] = m[0] - m[i]
        m[0] = m[0] - m[i]
        heapsize -= 1
        heapify(m, 0, heapsize)


heapsort(m, heapsize)
print(m)
