def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(0, number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(quick_pick)


def generate_quick_pick():
    import random
    numbers = [n for n in range(1, 46)]
    quick_pick = []
    for i in range(0, 6):
        rand_index = random.randint(0, len(numbers))
        rand_number = [numbers[rand_index]]
        numbers.remove(int(rand_number[0]))
        quick_pick = quick_pick + rand_number
    return quick_pick


main()
