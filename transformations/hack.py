
flag = ""

with open("enc", "r") as f:
	s = f.read()
	for ch in s:
		val = ord(ch)
		flag += chr(val >> 8)
		flag += chr(val & 0xff)
print(flag)
