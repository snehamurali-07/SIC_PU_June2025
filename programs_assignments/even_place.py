num = input("Enter a number: ")

sum_even_place = 0

for i in range(len(num)):      # len() function is used for strings and not for integer
    if (i + 1) % 2 == 0:  
        sum_even_place += int(num[i])    # type casted to int because a string and integer cannot be added

print("Sum of digits at even positions:", sum_even_place)