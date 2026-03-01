text = input("Enter input: ")

i = 0
result = ""

while i < len(text):
    ch = text[i]

    if 'a' <= ch <= 'z':
        result += ch.upper()
    elif 'A' <= ch <= 'Z':
        result += ch.lower()
    else:
        result += ch

    i += 1

print("Output:", result)