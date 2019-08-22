"""

CP1404/CP5632 - Practical

Pseudocode for temperature conversion

"""

MENU = """C - Convert Celsius to Fahrenheit

F - Convert Fahrenheit to Celsius

Q - Quit"""

print(MENU)

choice = input(">>> ").upper()


def celsius_to_fahren():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def fahren_to_celsius():
    global celsius
    celsius = (fahrenheit - 32) * 5 / 9.0


while choice != "Q":

    if choice == "C":

        celsius = float(input("Celsius: "))

        celsius_to_fahren()

        print("Result: {:.2f} F".format(fahrenheit))

    elif choice == "F":

        farenheit = float(input("Fahrenheit: "))

        fahren_to_celsius()

        print("Result: {:.2F} C".format(celsius))

        # Hint: celsius = 5 / 9 * (fahrenheit - 32)

        # Remove the "pass" statement when you are done. It's a placeholder.

    else:

        print("Invalid option")

    print(MENU)

    choice = input(">>> ").upper()

print("Thank you.")
