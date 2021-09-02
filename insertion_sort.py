from binary_search import binary_search


def insertion_sort(array):

    for i in range(1, len(array)):
        last = array[i]
        j = i - 1
        while j >= 0 and array[j] > last:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = last


def recursion_insertion_sort(array, n):

    if n < 1:
        return

    recursion_insertion_sort(array, n-1)
    last = array[n-1]
    j = n - 2
    while j >= 0 and array[j] > last:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = last

    
def binary_insertion_sort(array):
    
    for i in range(1, len(array)):
        last = array[i]
        j = binary_search(array, last, 0, i)
        while j >= 0 and array[j] > last:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = last


if __name__ == '__main__':
    array = [5, 4, 3, 2, 1, 0]
    binary_insertion_sort(array)
    print(array)

    # array = [5, 4, 3, 2, 1]
    # recursion_insertion_sort(array, len(array))
    # print(array)
    
    
