word = input("Enter the word you wish to find: ")
strg = input("Enter a string you wish to search through: ")

found = True
start = 0

for ch in word :
    pos = strg.find(ch, start)
    if pos < 0:
        found = False
        break
    start = pos + 1
if found:
    print("Yes")
    
else:
    print("No")
