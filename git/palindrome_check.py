text = input("Enter word: ")
text = text.replace(' ','')

if len(text) > 1 and text.upper() == text[::-1].upper(): # text[::-1] - literuje słowo od końca
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
