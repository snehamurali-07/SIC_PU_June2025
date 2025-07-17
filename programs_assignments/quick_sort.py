def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    k = low

    for i in range(low, high):
        if arr[i] <= pivot:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1

    arr[k], arr[high] = arr[high], arr[k]
    return k  

arr = list(map(int, input("Enter array elements: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)