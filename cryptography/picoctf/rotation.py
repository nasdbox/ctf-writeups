data = "xqkwkbn{z0bib1wv_l3kzgxb3l_4k71n5j0}"



for i in range(1, 30):
    flag = ""
    for char in data:
        if not char.isalpha():
            flag += char
            continue
        val = ord(char)
        val -= 97
        val -= i 
        val %= 26
        val += 97
        flag += chr(val)
    print(flag)
