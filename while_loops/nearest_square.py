"""
Nearest Square
Write a while loop that finds the largest square number less than an
integer 'limit' and stores it in a variable 'nearest_square'.
A square number is the product of an integer multiplied by itself,
for example 36 is a square number because it equals 6*6.

For example, if limit is 40, your code should set the nearest_square to 36.
"""

limit = 40

# write your while loop here
"""
1. while num < limit:
    -> multiply num by itself and assign to nearest_square
    -> increment num by 1
    -> the loop will use the new num to check against limit
    -> assign variable 'nearest_square' to i
    -> print result 
"""
nearest_square = 1
num = 1
while nearest_square <= limit:
    print(f"start num: {num}, nearest_square: {nearest_square}")
    num += 1
    if (num * num) > limit:
        break
    else:
        nearest_square = num * num
    print(f"num: {num}, nearest_square: {nearest_square}")
print(nearest_square)


# another method without the loops
import math

root = math.isqrt(limit)
nearest_square = root * root
print(nearest_square)





