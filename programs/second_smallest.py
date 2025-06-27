num = input("Enter a number: ")

digits = []
for ch in num:
    digits.append(int(ch))    

unique_digits = list(set(digits))
unique_digits.sort()

if len(unique_digits) < 2:
    print("There is no second smallest digit.")
else:
    print("Second smallest digit is:", unique_digits[1])
