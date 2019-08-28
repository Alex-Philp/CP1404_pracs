numbers = []
total = 0
for i in range(1,6):
    number = [int(input("Number: "))]
    numbers = numbers + number

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))

numbers.sort()
print("The smallest number is {}".format(numbers[0]))
print("The largest number is {}".format(numbers[-1]))

print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))