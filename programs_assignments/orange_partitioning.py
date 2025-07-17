'''
;ast orange in Tisha's hand
all orange smaller than the orange in her hand - childeren
all orange bigger than the orange in her hand -  sell
'''

def orange_partition(arr):
    n = len(arr)
    k = 0
    for i in range(n-1):
        if arr[i] <= arr[n-1]:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
    arr[k], arr[n-1] = arr[n-1], arr[k]
    print(arr)

numOfOranges = int(input())
sizes = list(map(int, input().split()))
result = orange_partition(sizes)
print(result)