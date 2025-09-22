"""
Question: What type of loop should we use?
You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

Would you use a while or a for loop to write this code?
"""

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_num = []

for num in num_list:
    if num % 2 != 0:
        odd_num.append(num)
        if len(odd_num) > 4:
            break
print(odd_num)
print(sum(odd_num))

# using comprehensions

odd_nums = [n for n in num_list if n % 2 != 0][:5]
print(sum(odd_nums))
