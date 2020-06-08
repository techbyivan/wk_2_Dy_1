word = input("Give me a word yo...\n")

word_list = {}
for letter in word:
    if letter in word_list:
        word_list[letter] += 1
    else:
        word_list[letter] = 1
    
print(word_list)