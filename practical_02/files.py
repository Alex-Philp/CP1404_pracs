"""Write code that asks the user for their name, then opens a file called "name.txt"
 and writes that name to it.
Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
Create a text file called numbers.txt and save it in your prac_02 directory.
 Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write code that opens "numbers.txt", reads the numbers and adds them together
then prints the result, which should be... 59.
Now write a fourth block of code that can print the total for a file
 containing any number of numbers."""
OUTPUT_FILE = "name.txt"
name = input("What is your name: ")
output = open(OUTPUT_FILE, 'w')
print("{}".format(name), file=output)
output.close()

readable_name = open(OUTPUT_FILE, 'r')
name_from_file = readable_name.read()
print("Your name is {}".format(name_from_file))
readable_name.close()

number_file = open("number.txt", 'r')
number_1 = int(number_file.readline())
number_2 = int(number_file.readline())
result = number_1 + number_2
print(result)
