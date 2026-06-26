import hashlib
import sys

if len(sys.argv) < 2:
	print(f"Usage: python3 {sys.argv[0]} <sha256_hash>")
	sys.exit(1)

cnt = 0
found = 0
given_pass = sys.argv[1].strip()
with open("rockyou.txt", "r", encoding="latin-1") as f:
	for line in f:
		password = line.strip()
		# computing hash
		hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
		if hash == given_pass:
			print(f"\n[+] password found: {password}")
			found = 1
			break
		else:
			print(f"\rcracking password {cnt}...", end="")
			cnt += 1
	if not found:
		print(f"\r[-] Password not found in wordlist. Total checked: {cnt}")
