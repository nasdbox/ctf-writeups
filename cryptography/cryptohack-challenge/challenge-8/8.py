key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2and3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
enc = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1 = bytes.fromhex(key1)
key2and3 = bytes.fromhex(key2and3)
enc = bytes.fromhex(enc)

#print(key1)

flag_bytes = bytes(f^a^b for f, a, b in zip(enc, key1, key2and3))

print(flag_bytes.decode())
