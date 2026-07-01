output = "qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze"

flag = list(output)


for i in range(3):
    ls = [0]*len(output)
    for j in range(len(output)):
        a = (j % 0xff >> 1 & 0x55) + (j % 0xff & 0x55)
        a = ((a >> 2) & 0x33) + (a & 0x33)
        shift = (a >> 4) + (a & 0xf)
        b = ord(flag[j]) - 97
        input = (b - shift) % 26
        ls[j] = chr(input+97)

    flag = ls

print("".join(flag))

