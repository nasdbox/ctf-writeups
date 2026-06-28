
def eea(a, b):
	if b == 0:
		return a, 1, 0

	gcd, x1, y1 = eea(b, a%b)
	return gcd, y1, x1-(a//b)*y1

print(eea(3, 13))
