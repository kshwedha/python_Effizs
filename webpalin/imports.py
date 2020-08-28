
from cryptography import encrypt
from cryptography import decrypt

msg=raw_input("enter your message\n")
msg=str(msg)
key='this is my key'

encrypt_data=encrypt(key, msg)
decrypt_data=decrypt(key, encrypt_data)

print(repr(encrypt_data))
print(repr(decrypt_data))

