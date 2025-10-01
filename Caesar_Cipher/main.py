# TODO-1: Import and print the logo from art.py when the rpogram starts.
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#TODO-2: What happens if the user enters a numnber/symbols/space?

# TODO-C: Combine the encrypt and decrypt() function into a single function called caesar().
            # Use the value of the user chosen direction variable to determine which functionally to use.
            # call the caeser function instead of encrypt/decrypt and pass in all three vaiables
                    #direction/text/shift
def caesar(original_text,shift_amount, encode_or_decode):
    output_text = ""  #j
    
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount #7 -> 9
            shifted_position %= len(alphabet) #0 - 25  
            output_text+= alphabet[shifted_position] #j
        else:
            # Keep the character as is (e.g., spaces, punctuation)
            output_text += letter
    print(f"Here is the {encode_or_decode} result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?
while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again, type 'no':" ).lower()
    if restart == 'no':
        break
        print("Goodbye")
        