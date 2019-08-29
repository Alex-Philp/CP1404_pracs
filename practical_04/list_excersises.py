numbers = []
total = 0
for i in range(1, 6):
    number = [int(input("Number: "))]
    numbers = numbers + number

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))

numbers.sort()
print("The smallest number is {}".format(numbers[0]))
print("The largest number is {}".format(numbers[-1]))

print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

# woefully inadequate password checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_input = input("Please enter your username: ")
if username_input in usernames:
    print("Access Granted")
else:
    print("Access Denied")
