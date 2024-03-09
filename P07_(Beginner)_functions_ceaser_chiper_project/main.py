from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(start_text, cipher_direction, shift_no):
    ceaser_text = ''

    if cipher_direction == 'decode':
        shift_no *= -1

    for letter in start_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            decode_letter = alphabet[letter_index + shift_no]
            ceaser_text += decode_letter
        else:
            ceaser_text += letter
    print(f"Your Ceaser Text is: {ceaser_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = round(shift / 26)

    # shift = shift % 26
    ceaser(start_text=text, cipher_direction=direction, shift_no=shift)

    ask = input("Type 'YES' if you want to go again, otherwise 'NO'.\n").lower()
    if ask == 'no':
        should_continue = False
        print("Good Bye")


