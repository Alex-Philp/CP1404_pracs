"""

CP1404/CP5632 - Practical

Pseudocode for temperature conversion

"""

MENU = """C - Convert Celsius to Fahrenheit

F - Convert Fahrenheit to Celsius

Q - Quit"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9.0
    return celsius


def main():
    print(MENU)

    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "C":

            celsius = float(input("Celsius: "))

            fahrenheit = celsius_to_fahrenheit(celsius)

            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":

            fahrenheit = float(input("Fahrenheit: "))

            celsius = fahrenheit_to_celsius(fahrenheit)

            print("Result: {:.2F} C".format(celsius))

        # Hint: celsius = 5 / 9 * (fahrenheit - 32)

        # Remove the "pass" statement when you are done. It's a placeholder.

        else:

            print("Invalid option")

        print(MENU)

        choice = input(">>> ").upper()

    print("Thank you.")


main()
