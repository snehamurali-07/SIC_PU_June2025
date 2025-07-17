lines = int(input("Enter number of lines: "))
print("\nA. Right-Angled Triangle")
for i in range(1, lines + 1):
    print('*' * i)

print("\nB. Equilateral Triangle")
for i in range(1, lines + 1):
    print(' ' * (lines - i) + '* ' * i)

print("\nC. Hollow Square")
for i in range(lines):
    if i == 0 or i == lines - 1:
        print('*' * lines)
    else:
        print('*' + ' ' * (lines - 2) + '*')

print("\nD. Hollow Rhombus")
for i in range(lines):
    print(' ' * (lines - i - 1), end='')
    if i == 0 or i == lines - 1:
        print('*' * lines)
    else:
        print('*' + ' ' * (lines - 2) + '*')


print("\nF. X Shape")
for i in range(lines):
    for j in range(lines):
        if j == i or j == lines - 1 - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

