alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
	word_encoded = True
	cipher_text = " "
	for i in start_text:
		if cipher_direction == "encode":
			cipher_text += alphabet[(alphabet.index(i) + shift) % 26]			
			
	
		elif cipher_direction == "decode":
			cipher_text += alphabet[(alphabet.index(i) - shift) % 26]			
			word_encoded = False

	if (word_encoded):
		print(f"The encoded text is {cipher_text}")
	else:
		print(f"The decoded text is {cipher_text}")

caesar(text, shift, direction)