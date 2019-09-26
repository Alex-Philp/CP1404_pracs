from practical_06.guitar import Guitar

print("My guitars")
guitars = []
name = input("Name: ")
year = int(input("Year: "))
cost = float(input("Cost: "))
i = 0
while name != "":
    guitars.append(Guitar(name, year, cost))
    print("{} ({}) : ${:.2f} added.".format(guitars[i].name, guitars[i].year, guitars[i].cost))
    i += 1
    name = input("Name: ")
    if name != "":
        year = input("Year: ")
        cost = input("Cost: ")
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {} ({}), worth $ {:.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
