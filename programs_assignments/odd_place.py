num = input("Enter a number: ")

sum_odd_place = 0

for i in range(len(num)):
    if i % 2 == 1:  # Odd index
        digit = int(num[i])
        if digit % 2 == 0:  # Even digit
            sum_odd_place += digit

print("Sum of even digits at odd indices:", sum_odd_place)

