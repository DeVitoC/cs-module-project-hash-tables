# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
def crack_caesar(filename):
	with open(filename) as f:
		words = f.read()

	reference = {}
	known_letter_frequency_order = "ETAOHNRISDLWUGFBMYCPKVQJXZ"
	text_to_decode = words.translate(str.maketrans('', '', '":;,.—-+=/\|[]{}()*^&!? \n\''))
	text_to_decode = text_to_decode.lower()
	text_to_decode = list(text_to_decode)

	for char in text_to_decode:
		if char.isdigit():
			continue
		if char in reference.keys():
			reference[char] += 1
		else:
			reference[char] = 1

	sorted_array = sorted(reference.items(), key = lambda x: x[1], reverse = True)
	cipher_str = ""

	for item in sorted_array:
		cipher_str += item[0].upper()

	new_text = words.translate(str.maketrans(cipher_str, known_letter_frequency_order, ""))
	print(new_text)

crack_caesar("ciphertext.txt")
