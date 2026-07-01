"""
after running the nc multiple times we saw that N is even which is not possible because p and q are both prime numbers but this is possible because there is an even prime number exist
p = 2, q = N // 2
further we can calculate phi = (p-1) * (q-1)
then we can calculate d which is a private key to decrypt the message
"""

from Crypto.Util.number import long_to_bytes, inverse

e = 65537
c = 14403548942422461413000730090283331866445291661221298017103909939910404382717241903503593083009579964628664743935898304276630292473800930369752032554401829
N = 16169493804075322505766844311672826028783999189806470054160015898597411213813607827662536082693843335949875386711273418168322541287934899509740868671935274

p = 2
q = N//2

phi = (p-1) * (q-1)

# d = inverse(e, phi)
d = pow(e, -1, phi)

dec = pow(c, d, N)

ans = long_to_bytes(dec).decode("utf-8")

print(ans)


