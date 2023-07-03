text1 = input("Enter text nr 1: ")
text2 = input("Enter text nr 2: ")
text1x = ''.join(sorted(list(text1.upper().replace(' ',''))))
text2x = ''.join(sorted(list(text2.upper().replace(' ',''))))

if len(text1x) > 0 and text1x == text2x:
    print("Texts are anagrams. ")
else:
    print("Texts are not anagrams. ")
