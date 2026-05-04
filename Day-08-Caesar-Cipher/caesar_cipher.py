alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encoder(text, shift):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result += alphabet[(index + shift) % 26]
        else:
            result += char
    return result

def decoder(text, shift):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result += alphabet[(index - shift) % 26]
        else:
            result += char
    return result

if __name__ == "__main__":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(f"Encoded: {encoder(text, shift)}")
    elif direction == "decode":
        print(f"Decoded: {decoder(text, shift)}")
    else:
        print("Not a valid direction")
