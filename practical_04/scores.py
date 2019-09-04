"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    for i in range(0,len(subjects)):
        print(subjects[i], "Scores:")
        for score in score_values[2*i]:
            print("{:>2}".format(score))
        for score in score_values[2*i+1]:
            print("{:>2}".format(score))
        if max(score_values[2*i]) > max(score_values[2*i+1]):
            print("Max: {:3}".format(max(score_values[2*i])))
        else:
            print("Max: {:3}".format(max(score_values[2*i+1])))

        if min(score_values[2*i]) < min(score_values[2*i+1]):
            print("Min: {:3}".format(min(score_values[2*i])))
        else:
            print("Min: {:3}".format(min(score_values[2*i+1])))

        average = sum(score_values[2*i] + score_values[2*i+1]) / len(score_values[2*i] + score_values[2*i+1])
        print("Average: {:6.2F}".format(average))
        print()

main()