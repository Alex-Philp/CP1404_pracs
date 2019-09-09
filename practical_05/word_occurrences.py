text = input("Text: ")
word_to_count = {}
words = text.split(" ")
for word in words:
    if word.lower() in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word.lower()] = 1
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
words = list(word_to_count.keys())
words.sort()
print("Text: {}".format(text))
for word in words:
    print(("{:{}} : {}".format(word, len(longest_word), word_to_count[word])))
