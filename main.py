alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
	word_encoded = True
	cipher_text = " "
	for i in start_text:
		if cipher_direction == "decode":
			shift_amount = shift_amount * -1
			word_encoded = False
		cipher_text += alphabet[(alphabet.index(i) + shift) % 26]			


	if (word_encoded):
		print(f"The encoded text is {cipher_text}")
	else:
		print(f"The decoded text is {cipher_text}")

caesar(text, shift, direction)