alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
again = ''


def encrypt(text, shift):
    encwrd = ""
    for i in text:
        position = alphabet.index(i)
        post = (position + shift) % 26
        encwrd += alphabet[post]

    print(f"The encoded text is {encwrd}")


def decrypt(text, shift):
    decwrd = ""
    for i in text:
        position = alphabet.index(i)
        post = (position - shift) % 26
        decwrd += alphabet[post]

    print(f"The decoded text is {decwrd}")

print(""" 
 ______                          _        
|  ____|                        | |
| |__    _ __    ___   ___    __| |  ___
|  __|  | '_ \\  / __| / _ \  / _` | / _ \\
| |____ | | | || (__ | (_) || (_| ||  __/
|______||_| |_| \___| \___/  \__,_| \___|
             _____                          _
            |  __ \\                        | |
            | |  | |  ___   ___   ___    __| |  ___
            | |  | | / _ \\ / __| / _ \\  / _` | / _ \\
            | |__| ||  __/| (__ | (_) || (_| ||  __/
            |_____/  \___| \___| \___/  \__,_| \___|\n\n""")

while again != 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid Input...Try Again...")

    again = input("Do you want to continue this again? (yes/no): ")
