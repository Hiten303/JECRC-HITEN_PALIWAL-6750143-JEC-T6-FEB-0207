## WAP to take a character from the user and convert it into lowercase if it is in uppercase or vice-versa

character = input('Enter input: ')

if character >='a' and character <='z':
    print(chr(ord(character)-32))
elif character >='A' and character <='Z':
    print(chr(ord(character)+32))
else:
    print("Not an alphabet",character)