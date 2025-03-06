alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from pi_art import caesar_logo
print(caesar_logo)

go_on = True

while go_on == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    def ceasar(plain_text, shift_amount, direct):
        display = ""
        if direct == "decode":
                shift_amount *= -1
        for letters in plain_text:
            if letters in alphabet:
                position = alphabet.index(letters)
                new_position= position + shift_amount
                display+= alphabet[new_position]
            else:
                display+= letters

        print(f"Your {direct}d text is {display}")


    ceasar(plain_text= text, shift_amount= shift, direct = direction)
    letsgo = input("Type 'yes' if you want to go again, otherwise type 'no':\n").lower()

    if letsgo == 'no':
         go_on = False
    elif letsgo == "yes":
         go_on = True

