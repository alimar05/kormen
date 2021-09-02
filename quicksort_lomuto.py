def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array


def partition(array, l, r):
    p = array[l]
    i = l + 1
    for j in range(l+1, r+1):
        if array[j] < p:
            swap(array, i, j)
            i += 1
    swap(array, l, i-1)
    return i-1


def quicksort(array, l, r):

    if l < r:
        i = partition(array, l, r)
        quicksort(array, l, i-1)
        quicksort(array, i+1, r)


if __name__ == '__main__':
    array = [3, 8, 2, 5, 1, 4, 7, 6, 9, 10] 
    print(array)
    quicksort(array, 0, len(array)-1)
    print(array)
