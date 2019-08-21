password = str(input("Thing "))
number = 0
length = len(password)

print(length)

for char in password:
    output = char.isalpha()
    if output is True:
        number += 1
try:
    print(number)
except ValueError:
    print("Can't do it")
