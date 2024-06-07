def encode(text, number):
    encoded_text = []
    for char in text:
        if char != " ":
            asciivalue = ord(char) + number
            encoded_text.append(chr(asciivalue))
        else:
            encoded_text.append(char)
    print("".join(encoded_text))

def decode(text, number):
    decoded_text = []
    for char in text:
        if char !=" ":
            asciivalue = ord(char) - number
            decoded_text.append(chr(asciivalue))
        else:
            decoded_text.append(char)
    print("".join(decoded_text))

loop = True
while loop:
    option = input("Enter encode or decode to proceed, else exit: ").lower()
    if option != "exit":
        changingText = input("Enter the text you want to change: ")
        shiftNumber = int(input("Enter the shift number: "))
        if shiftNumber >= 0:
            if option == "encode":
                encode(changingText, shiftNumber)
            elif option == "decode":
                decode(changingText, shiftNumber)
    else:
        loop = False
