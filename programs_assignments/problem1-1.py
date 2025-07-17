original_str = input().lower().strip()
rotated_str = input().lower().strip()

def isSameReflection():
    if len(original_str) != len(rotated_str):
        print(-1)
    else:
        temp = rotated_str * 2
        print(temp)
        if original_str in temp:
            print(1)
        else:
            print(-1)

isSameReflection()