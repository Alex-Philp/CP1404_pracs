text = input("Text: ")
word_to_count = {}
words = text.split(" ")
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
strings = []
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

for word, count in word_to_count.items():
    strings.append(("{:{}} : {}".format(word, len(longest_word),word_to_count[word])))
strings.sort()
print("Text: {}".format(text))
for string in strings:
    print(string)
