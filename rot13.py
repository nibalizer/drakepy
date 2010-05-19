def rot13_character(character):
	# Simple Rot13 stuff
	a = ord('a')
	z = ord('z')
	A = ord('A')
	Z = ord('Z')
	
	code = ord(character)
	#Rotate lower-case chars
	if a <= code <= z:
		code = a + (code - a + 13) % 26
	# Rotate upper-case chars
	elif A <= code <= Z:
		code = A + (code - A + 13) %26
	#Leave other chars alone
	else:
		pass
	return chr(code)

def rot13(plaintext):
	#Loop over letters in the text.
	ciphertext = ""
	for character in plaintext:
		ciphertext += rot13_character(character)
	return ciphertext


