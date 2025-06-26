# Count number of prime digits in a number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10
    if digit in [2, 3, 5, 7]:
        count += 1
    num //= 10

print("Number of prime digits:", count)
