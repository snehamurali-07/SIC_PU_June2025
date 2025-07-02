def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid  # Found the target
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Not found

arr = list(map(int, input("Enter array elements: ").split(',')))
key = int(input("Enter the key to search: "))
print("Iterative method - Key found at", binary_search_iterative(arr, key))


def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1  # Base case: not found

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid  # Found
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, high)
    else:
        return binary_search_recursive(arr, key, low, mid - 1)

low = 0
high = len(arr) - 1

print("Recursive method - Key found at", binary_search_recursive(arr, key, low, high))