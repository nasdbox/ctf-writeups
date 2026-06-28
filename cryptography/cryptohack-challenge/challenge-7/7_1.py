from pwn import *

data = "label"

flag = xor(data.encode(), 13).decode()

print(flag)
