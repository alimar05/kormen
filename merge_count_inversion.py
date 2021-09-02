def split_sort_count_inv(left_sort, right_sort):

    i, j = 0, 0
    split_sort = []
    split_count_inv = 0
    while i < len(left_sort) and j < len(right_sort):

        if left_sort[i] <= right_sort[j]:
            split_sort.append(left_sort[i])
            i += 1
        else:
            split_sort.append(right_sort[j])
            j += 1

            split_count_inv += len(left_sort) - i

    while i < len(left_sort):
        split_sort.append(left_sort[i])
        i += 1
    while j < len(right_sort):
        split_sort.append(right_sort[j])
        j += 1

    return split_sort, split_count_inv


def sort_count_inv(array):

    if len(array) == 0 or len(array) == 1:
        return array, 0
    else:

        middle = len(array) // 2
        
        left_sort, left_count_inv = sort_count_inv(array[:middle])
        right_sort, right_count_inv = sort_count_inv(array[middle:])

        split_sort, split_count_inv = split_sort_count_inv(left_sort, right_sort)

        return split_sort, left_count_inv + right_count_inv + split_count_inv 


print(sort_count_inv([1, 3, 5, 2, 4, 6]))
