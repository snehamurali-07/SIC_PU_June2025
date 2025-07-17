# Find the Nth Fibonacci term (1st = 1, 2nd = 2)
n = int(input("Enter the value of N: "))
if n == 1:
    print("Fibonacci term:", 1)
elif n == 2:
    print("Fibonacci term:", 2)
else:
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    print("Fibonacci term:", b)
