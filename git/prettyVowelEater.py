word_without_vowels = ""
user_word = input("Enter a word:")
user_word = user_word.upper()
for letter in user_word:
    if letter in "EAUIO":
        continue
    word_without_vowels += letter
print(word_without_vowels)
