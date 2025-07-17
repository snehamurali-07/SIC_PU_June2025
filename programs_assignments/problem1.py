original_str = input()
rotated_str = input()

if len(original_str) != len(rotated_str):
    print(-1)
else:
    temp = rotated_str * 2
    if original_str in temp:
        print(1)
    else:
        print(-1)
