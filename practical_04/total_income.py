"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_income_report(incomes, number_of_months)


def print_income_report(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        total += incomes[month - 1]
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, incomes[month - 1], total))


main()
