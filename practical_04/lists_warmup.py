numbers = [3, 1, 4, 1, 5, 9, 2]
# 3, 2, 1, [3, 2] (answer = [3, 1, 4, 1, 5, 9]),
# [4, 1] (answer = [1]), True, False, False,
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# numbers[0]
# numbers[-1]
# numbers[3]
# numbers[:-1]
# numbers[3:4]
# 5 in numbers
# 7 in numbers
# "3" in numbers
# numbers + [6, 5, 3]

numbers[0] = 10
print(numbers)
numbers[-1] = 1
print(numbers)
new_numbers = numbers[2:]
print(new_numbers)
answer = 9 in numbers
print(answer)
