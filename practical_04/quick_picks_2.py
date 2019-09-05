import random


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(0, number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(
            "{:2} {:2} {:2} {:2} {:2}".format(quick_pick[0], quick_pick[1], quick_pick[2], quick_pick[3],
                                              quick_pick[4]))


def generate_quick_pick():
    length = 45
    quick_pick = []
    for i in range(0, 6):
        random_number = [random.randint(1, length)]

        while random_number[0] in quick_pick:
            random_number = [random.randint(1, length)]

        quick_pick = quick_pick + random_number

    quick_pick.sort()
    return quick_pick


main()
