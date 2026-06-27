from Crypto.Util.number import *

base_ten = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

bytes_data = long_to_bytes(base_ten)

hex_data = bytes_data.hex()

# print(type(hex_data))

flag = ""

for i in range(0, len(hex_data), 2):
    s = hex_data[i] + hex_data[i+1]
    num = int(s, 16)
    flag += chr(num)

print(flag)
