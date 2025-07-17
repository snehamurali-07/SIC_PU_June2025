def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        initial = i

        for j in range(i + 1, n):
            if arr[j] < arr[initial]:
                initial = j

        # Swap if needed
        arr[i], arr[initial] = arr[initial], arr[i]

    print("Selection sort:", arr)


# Input
arr = list(map(int, input("Enter elements: ").split()))
selection_sort(arr)
