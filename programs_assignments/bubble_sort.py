def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # swap

    print("Bubble Sort:", arr)



def optimised_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        is_sorted = True  # Assume the list is already sorted

        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False

        if is_sorted:
            break  # Exit early if no swaps happened

    print("Optimised Bubble Sort:", arr)


arr = list(map(int, input("Enter elements: ").split()))
bubble_sort(arr)
optimised_bubble_sort(arr)