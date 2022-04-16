from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
from Crypto.PublicKey import RSA


with open('flag.txt', 'rb') as fd:
    flag = fd.read().strip()

p = getPrime(4096)
q = getPrime(4096)
n = p*q
e = 3

rsakey = RSA.construct((n,e))
with open('pub.key', 'wb') as fd:
    fd.write(rsakey.export_key())

ciphertext = long_to_bytes(pow(bytes_to_long(flag), e, n))
with open('flag.txt.enc', 'wb') as fd:
    fd.write(ciphertext)
