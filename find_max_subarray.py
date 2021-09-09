def find_max_subarray_bruteforce(array):

    idx_left_max_subarray = 0
    idx_right_max_subarray = 0
    max_sum_subarray = -10e999

    i = 0
    for elemi in array:
        sum_subarray = elemi
        j = 0
        for elemj in array:
            if j > i:
                sum_subarray += elemj
                if sum_subarray > max_sum_subarray:
                    max_sum_subarray = sum_subarray
                    idx_left_max_subarray = i
                    idx_right_max_subarray = j
            j += 1
        i += 1

    return idx_left_max_subarray, idx_right_max_subarray, max_sum_subarray


def find_max_crossing_subarray(low, right, mid, array):
    
    sum = 0
    left_sum = -10e999
    idx_left_max = 0
    
    i = mid
    while i >= low:
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            idx_left_max = i
        i -= 1

    sum = 0
    right_sum = -10e999
    idx_right_max = 0

    i = mid + 1
    while i <= right:
        sum += array[i]
        if sum > right_sum:
            right_sum = sum
            idx_right_max = i
        i += 1
    
    return idx_left_max, idx_right_max, left_sum + right_sum


def find_max_subarray_divide_rule(low, high, array):
    
    if low == high:
        return low, high, array[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray_divide_rule(low, mid, array)
        right_low, right_high, right_sum = find_max_subarray_divide_rule(mid+1, high, array)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(low, high, mid, array)
        if left_sum > cross_sum and left_sum > right_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_subarray_divide_rule_bruteforce(low, high, array):
    
    if high - low + 1 == 20:
        return find_max_subarray_bruteforce(low, high, array)
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray_divide_rule(low, mid, array)
        right_low, right_high, right_sum = find_max_subarray_divide_rule(mid+1, high, array)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(low, high, mid, array)
        if left_sum > cross_sum and left_sum > right_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
            

if __name__ == '__main__':
    import time
   
    
    # array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, 1, 2, 3, 4, 5, 6, 7]
    t0 = time.monotonic()
    print(find_max_subarray_bruteforce(array))
    print(find_max_subarray_divide_rule(0, len(array)-1, array))
    print(find_max_subarray_divide_rule_bruteforce(0, len(array)-1, array))
    print('{0:.10f}'.format(time.monotonic()-t0))
