def binary_search(array, value, low, high):
    
    while low <= high:
        mid = (low+high) // 2
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            high = mid - 1
        else:
            low = mid + 1

            
def recursion_binary_search(array, value, low, high):
    
    mid = (low+high) // 2
    if value == array[mid]:
        return mid
    elif value < array[mid]:
        return recursion_binary_search(array, value, low, mid-1)
    else:
        return recursion_binary_search(array, value, mid+1, high)
            

if __name__ == '__main__':
    
    array = [1, 2, 3, 4, 5, 6]
    low = 0
    high = len(array) - 1
    print(binary_search(array, 9, low, high))
    print(recursion_binary_search(array, 6, low, high))