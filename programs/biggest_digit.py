# Find the biggest digit in a number using loop
num = int(input("Enter a number: "))

max_digit = 0
while num > 0:
    digit = num % 10    # one's place
    if digit > max_digit:
        max_digit = digit
    num //= 10    

print("Biggest digit:", max_digit)
