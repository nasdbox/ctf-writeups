import base64

hex_data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes_data = bytes.fromhex(hex_data)

decoded_bytes = base64.b64encode(bytes_data).decode()

print(decoded_bytes)
