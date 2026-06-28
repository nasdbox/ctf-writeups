ls = [14, 6, 11]

p = 29

for i in range(1, p):
	x = i*i % p
	if x in ls:
		print(i, p-i)
