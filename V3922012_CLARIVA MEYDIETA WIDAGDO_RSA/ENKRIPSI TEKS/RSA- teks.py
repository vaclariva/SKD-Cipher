#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair():
    p = q = 0
    while not is_prime(p):
        p = random.randint(10**3, 10**4)
    while not is_prime(q) or q == p:
        q = random.randint(10**3, 10**4)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calculate d, the modular multiplicative inverse of e (mod phi)
    d = pow(e, -1, phi)

    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

def decrypt(cipher_text, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return decrypted_message

# Example usage:
message = "Hello, namaku clariva"
public_key, private_key = generate_keypair()

# Encryption
cipher_text = encrypt(message, public_key)
print("Encrypted:", cipher_text)

# Decryption
decrypted_message = decrypt(cipher_text, private_key)
print("Decrypted:", decrypted_message)


# In[ ]:




