import secrets
from Crypto.Cipher import AES
import rsa

def generate_aes_key():
    # Generate AES key
    aeskey = secrets.token_bytes(32)
    print("\nAES Key: ", aeskey)
    return aeskey

def generate_rsa_keys():
    # Generate RSA public/private key pair
    publickey, privatekey = rsa.newkeys(1024)
    print("\nRSA Public Key:", publickey)
    print("\nRSA Private Key:", privatekey)
    return publickey, privatekey

def aes_encrypt(message, aeskey, aes_layers):
    # Encrypt message using AES encryption
    cipher = AES.new(aeskey, AES.MODE_GCM)
    nonce = cipher.nonce
    for i in range(aes_layers):
        if isinstance(message, str):
            message = message.encode("utf-8")
        aes_ciphertext = cipher.encrypt(message)
        print("\nAES Ciphertext -", i+1, ":", aes_ciphertext)
        message = aes_ciphertext  # set message for next iteration
    return nonce, aes_ciphertext

def rsa_encrypt(aes_ciphertext, publickey):
    # Encrypt message using RSA encryption
    rsa_ciphertext = rsa.encrypt(aes_ciphertext, publickey)
    print("\nEncrypted message by RSA:", rsa_ciphertext)
    return rsa_ciphertext

def rsa_encrypt_aeskey(aeskey, publickey):
    # Encrypt AES key using RSA encryption
    cipherkey = rsa.encrypt(aeskey, publickey)
    print("\nEncrypted AES Key:", cipherkey)
    return cipherkey

def rsa_decrypt_aeskey(cipherkey, privatekey):
    # Decrypt AES key using RSA decryption
    decryptedkey = rsa.decrypt(cipherkey, privatekey)
    print("\nDecrypted AES Key:", decryptedkey)
    return decryptedkey

def rsa_decrypt(aes_decrypted, privatekey):
    # Decrypt message using RSA decryption
    rsa_decrypted = rsa.decrypt(aes_decrypted, privatekey)
    print("\nDecrypted message by RSA:", rsa_decrypted)
    return rsa_decrypted

def aes_decrypt(nonce, ciphertext, decryptedkey,aes_layers):
    # Decrypt message using AES decryption
    cipher = AES.new(decryptedkey, AES.MODE_GCM, nonce=nonce)
    for i in reversed(range(0,aes_layers)):
        aes_decrypted = cipher.decrypt(ciphertext)
        if(i==0):
            aes_decrypted = aes_decrypted.decode("utf-8")
        print("\nDecrypted message by AES - ",i+1," :" ,aes_decrypted)
        ciphertext = aes_decrypted  # set message for next iteration
    return aes_decrypted


# Input message from user
message = input("\nEnter the message: ")
# Generate AES key
aeskey = generate_aes_key()
# Generate RSA public/private key pair
publickey, privatekey = generate_rsa_keys()

#Number of aes layers
aes_layers = int(input("\nEnter Number of AES Layers: "))

# Encrypt message using AES encryption
nonce, ciphertext = aes_encrypt(message, aeskey,aes_layers)
# Encrypt message using RSA encryption
ciphertext_rsa = rsa_encrypt(ciphertext, publickey)
# Encrypt AES key using RSA encryption
cipherkey = rsa_encrypt_aeskey(aeskey, publickey)


# Decrypt AES key using RSA decryption
decryptedkey = rsa_decrypt_aeskey(cipherkey, privatekey)
# Decrypt message using RSA decryption
decrypted_rsa = rsa_decrypt(ciphertext_rsa, privatekey)
# Decrypt message using AES decryption
decrypted = aes_decrypt(nonce, ciphertext, decryptedkey,aes_layers)


print("\n....................SUMMARY..........................\n")
print("\nMessage: ",message)
print("\naeskey: ",aeskey)
print("\nEncrypted AES key: ",cipherkey)
print("\nEncrypted message by AES: ",ciphertext)
print("\nEncrypted ciphertext by RSA: ",ciphertext_rsa)
print("\nDecrypted AES key by RSA: ",decryptedkey)
print("\nDecrypted message by RSA: ",decrypted_rsa)
print("\nDecrypted message by AES: ",decrypted)
