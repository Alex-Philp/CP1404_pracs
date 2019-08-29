def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(0, number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(quick_pick)


def generate_quick_pick():
    import random
    length = 45
    quick_pick = []
    for i in range(0, 6):
        rand_number = [random.randint(1, length)]

        while rand_number[0] in quick_pick:
            rand_number = [random.randint(1, length)]

        quick_pick = quick_pick + rand_number

    quick_pick.sort()
    return quick_pick


main()
