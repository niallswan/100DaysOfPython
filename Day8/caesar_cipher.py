import art

# Alphabet doubled up to handle letters near the end of the alphabet needing shifted
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

def caesar(plain_text, shift_amount, choice):
    # Turn shift amount negative if decoding
    if choice == "decode":
        shift_amount *= -1
    end_text = ""
    # For each letter in the text input
    for char in plain_text:
        if char in alphabet:
            # Find first index of the letter in the alphabet
            pos = alphabet.index(char)
            # Add new letter from shifted index to encrypted text
            end_text += alphabet[pos+shift_amount]
        # If char not in alphabet just add to text
        else:
            end_text += char
    print(f"The encrypted text is: {end_text}")

should_continue = True

while should_continue:
    # Prompt user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Use modulo to constrain the shift number to the range of the alphabet
    shift = shift % 26

    caesar(text, shift, direction)

    # Continue?
    result = input("Do you want to continue? y/n\n").lower()
    if result == "n":
        should_continue = False
        print("Exiting...")

