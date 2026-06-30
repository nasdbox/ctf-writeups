import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

flag = "fegdeogdgecoeocgcgchcfcffccfca"



# key is from 0 to 15
def decrypt_shift(key):
	ans = ""
	for i in flag:
		t1 = ord(i) - 97
		ans += ALPHABET[(t1-key)%16]
	
	return ans

def decrypt_flag(key):
	ans = ""
	val = decrypt_shift(key)
	# print(val)
	for i in range(0, len(val)-1, 2):
		a = val[i]
		b = val[i+1]
		num_a = ord(a) - 97
		num_b = ord(b) - 97
		binary = "{0:04b}{1:04b}".format(num_a, num_b)
		res = int(binary, 2)
		res = chr(res)
		ans += str(res)
		# byte = (num_a << 4) | num_b
		# ans += chr(byte)
	return ans

for i in range(16):
	print(decrypt_flag(i))
