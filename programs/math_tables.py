# print tables of a given number 
num = int(input("Enter the number:"))
for i in range (1,11):
    print("%2d * %02d = %03d" % (num, i, (num*i)))  # formatting done, for readability