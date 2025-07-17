def my_function(param1, param2):
    return param1 + param2

num1 = 49
num2 = 68
print(f'Num1={num1}, Num2={num2}')
result = my_function(num1, num2)
print(f'Result = {result}')



def my_function2(param1 = 37, param2 = 92): # default Args
    print(f'Num1={param1}, Num2={param2}')
    return param1 + param2

num1 = 49
num2 = 68

result = my_function2()
print(f'Result = {result}')

result = my_function2(num1)
print(f'Result = {result}')

result = my_function2(num1, num2)
print(f'Result = {result}')


'''
def my_function3(param1, param2 = 45): # default Args
    print(f'Num1={param1}, Num2={param2}')
    return param1 + param2

num1 = 49
num2 = 68

result = my_function3() # Not allowed
print(f'Result = {result}')

result = my_function3(num1) # 
print(f'Result = {result}')

result = my_function3(num1, num2)
print(f'Result = {result}')


'''
def my_function4(param1 = 84, param2 = 48): # default Args
    print(f'Num1={param1}, Num2={param2}')
    return param1 + param2

num1 = 49
num2 = 68

result = my_function4(num1, num2)
print(f'Result = {result}')

# result = my_function(param2 = num1, param2 = num2) ERROR
result = my_function4(param2 = num1, param1 = num2) # Named Params
print(f'Result = {result}')