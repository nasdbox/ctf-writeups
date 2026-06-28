data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

data_bytes = bytes.fromhex(data)

for i in range(255):
	possible_flag = bytes(x ^ i for x in data_bytes)
	try:
		dec = possible_flag.decode("utf-8")
		if "crypto" in dec:
			print(dec)
	except Exception as e:
		pass
