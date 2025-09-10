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
1. assign num to a value as 0 as the starting number
2. while nearest_square < limit:
    - > check first if the num + 1 multiplied by itself is larger than the limit
    - > if not, assign the product to the nearest_Square
    - > the loop will use the new num to check against limit
    - > assign variable 'nearest_square' to i
    - > print result 
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


# another method using while loops
"""
this method:
1. create a variable to store the num
2. while next number multiplied by itself (num + 1) ** 2 is less than limit:
    -> increment num
    -> assign the nearest_square to the num
"""

num = 0
while ((num + 1) ** 2) < limit:
    num += 1

nearest_square = num ** 2
print(nearest_square)



