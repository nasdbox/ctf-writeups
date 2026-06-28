
data = "0e0b213f2604"

data_bytes = bytes.fromhex(data)

evidence = "crypto"
evidence_bytes = evidence.encode()
#evidence_bytes = bytes(ord(char) for char in evidence)

flag_key = bytes(i^j for i, j in zip(data_bytes, evidence_bytes))

print(flag_key.decode())

flag_key = b"myXORkey"

decoded_flag_key = flag_key.decode()

challenge = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

challenge_bytes = bytes.fromhex(challenge)
"""
flag = ""
for i in range(0, len(challenge_bytes), 6):
	result = challenge_bytes[i:i+6]
	flag += bytes(j^k for j, k in zip(flag_key, result)).decode()

print(flag)
"""

flag_bytes = bytes(challenge_bytes[i] ^ flag_key[i%len(flag_key)] 
					for i in range(len(challenge_bytes)))

print(flag_bytes.decode())
