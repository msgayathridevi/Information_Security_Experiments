# pip install pycryptodome
from Crypto.Cipher import AES

def aes(pt, key):
    key = key.encode("ASCII")

    cipher = AES.new(key,AES.MODE_EAX)
    pt = pt.encode()

    ct = cipher.encrypt(pt)
    nonce = cipher.nonce

    decrypt = AES.new(key,AES.MODE_EAX,nonce=nonce)
    dt = decrypt.decrypt(ct)

    return ct,dt

pt = input("Enter the text : ")
key = input("Enter the key (16 bits) : ")
a,b = aes(pt, key)

print("Encryption")
print("cipher text : ", a)

print("----------------")

print("Decryption")
print("plain text : ", b)