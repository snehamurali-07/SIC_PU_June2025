n, x, y = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

group_y = arr[:y]  # less than p
group_x = arr[-x:] # more than p

max_y = max(group_y)
min_x = min(group_x)

print(min_x - max_y - 1) # number of elements
