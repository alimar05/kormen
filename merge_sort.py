def merge(left, right):

    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    
    return res


def merge_sort(numbers):

    if len(numbers) < 2:
        return numbers
    else:
        middle = len(numbers) // 2
        left_half = merge_sort(numbers[:middle])
        right_half = merge_sort(numbers[middle:])

        return merge(left_half, right_half)


print(merge_sort([5, 3, 8, 9, 1, 7, 0, 2, 6, 4]))