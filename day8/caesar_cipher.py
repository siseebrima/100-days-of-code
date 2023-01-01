from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(text, shift, direction):
  if shift > 0 and shift < 26:
    cipher_text = []
    if direction == 'decode':
      shift *= -1
  
    for c in text:
      if c not in alphabet:
        cipher_text.append(c)
        continue
      position = alphabet.index(c) + shift
      if position > 25:
        position = position - 26
      if position < 0:
        position = position + 26
      cipher_text.append(alphabet[position])
    cipher_text = ''.join(cipher_text)
    print(f'The {direction}d text is "{cipher_text}"')

  else:
    print("You have entered an invalid number. Shift should be between 1 and 25 (both inclusive)")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    rerun = input("Do you want to run the program again? 'yes' or 'no' ").lower()

    if rerun != 'yes':
        should_continue = False
        print("Goodbye")
