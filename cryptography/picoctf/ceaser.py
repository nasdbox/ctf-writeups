data = "dspttjohuifsvcjdpohatwvibg"

def solve(x):
	result = ""
	for i in range(len(data)):
		ch = ord(data[i])
		ch -= 97
		new_char_pos = ch - x
		new_char_pos = new_char_pos % 26
		new_char_pos += 97
		result += chr(new_char_pos)

	return result

for i in range(1, 30):
	print(solve(i))
