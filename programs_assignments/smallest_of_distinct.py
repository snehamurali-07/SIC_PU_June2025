# Find smallest of 3 distinct numbers
a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print(a, "is the smallest number")
elif b < a and b < c:
    print(b, "is the smallst number")
elif c < b and c < a:
    print(c, "is the smallest number")