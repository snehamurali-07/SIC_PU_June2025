'''import sys

print(sys.argv) # consids even the file name i.e.,'cla.py' aaa bbb ccc ddd
print(type(sys.argv))
print(type(sys.argv[0]))
print(len(sys.argv))
print(sys.argv[0]) #cla.py
print(sys.argv[-1]) #ddd
'''
import sys

print("STATE              CAPITAL")
print("--------------------------")

for arg in sys.argv[1:]:  # considers from index 1 i.e., the input from user and not the file name
    state, capital = arg.split()  # .split() splits the string by space
    print(f"{state.ljust(18)}{capital}")
