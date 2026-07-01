p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477
e = 65537
n = 948406957756830799684818171639547165784816468744946013083947881743680617123566349
c = 15341890103764929939105506004034128738090325640037083301857608662849501626260517

from Crypto.Util.number import inverse, long_to_bytes
# from pwn import *
# from pwnlib.util.fiddling import long_to_bytes

phi = (p-1) * (q-1)

# d = pow(e, phi-2, phi)
d = inverse(e, phi)

# Calculate the large number
final_ans = pow(c, d, n)


print(long_to_bytes(final_ans)[::-1].decode())
