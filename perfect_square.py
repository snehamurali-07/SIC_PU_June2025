# Check if a +ve integer is Perfect square
import math

def is_perfect_square(num):
    root = math.sqrt(num)
    return root * root == num

num = int(input())
if is_perfect_square(num):
    print(num, "is a perfect square")