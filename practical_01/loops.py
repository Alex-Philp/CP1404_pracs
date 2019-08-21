for i in range(1, 21, 2):
    print(i, end=' ')
print()


for i in range(0, 100, 10):
    print(i, end=' ')
print()


for i in range(20, 1, -1):
    print(i, end=' ')
print()

number=int(input("How many stars would you like to make? "))
for i in range (1, number, 1):
    print('*', end=' ')
print()

number=int(input("How many stars would you like to make? "))
for i in range (1, number, 1):
    for n in range (1, i, 1):
        print('*', end=' ')
print()

