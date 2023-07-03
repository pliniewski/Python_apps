# Caesar cipher. Encrypting message
text = input("Enter your message: ")

shift = 0

while shift == 0:
    try:
        shift = int(input("Enter cipher shift (1...25)"))
        if shift not in range (1, 26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Error shift value")

cipher = ''

for char in text:
    if  char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        code -= first
        code %= 26
        cipher += chr(code + first)
    else:
        cipher += char
    

print(cipher)
