strings = []
repeated_strings = []
string = input("Please enter some strings, finish by hitting the enter key with no input\n>>> ")
while not string == "":
    if string not in repeated_strings:
        if string in strings:
            repeated_strings.append(string)
        strings.append(string)
    string = input(">>> ")
print("Strings repeated", repeated_strings)
