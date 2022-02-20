from pwn import *
from binascii import unhexlify


def xor(a, b):
    return bytes(aa ^ bb for aa, bb in zip(a, b))

def pad(data, bsize):
    b = bsize - len(data) % bsize
    return data + bytes([b] * b)

address = ("babymac.sexy-allpacks.com", 10001)

conn = remote(address[0], address[1])
conn.recvuntil(b"> ").decode()

# First, ask server to sign empty string
print("Getting empty signature")
conn.sendline(b"sign")
conn.recvuntil(b"> ")
conn.sendline(b"")
emptySignature = bytes.fromhex(conn.recvuntil(b"> ").decode().split("\n")[0].strip())

# Now we construct the payload to sign
print("Signing payload")
flagCommand = pad(b"damelaflag", 16)
conn.sendline(b"sign")
# The payload is: first block - all 0x10, second block - all 0x00, third block is damelaflag string xored with empty signature
payload = b"\x10" * 16 + b"\x00" * 16 + xor(flagCommand, emptySignature)
conn.recvuntil(b"> ").decode()
conn.sendline(payload.hex())
correctSign = conn.recvuntil(b"> ").decode().split("\n")[0]

# And now we take signature of payload and send it to verify but this time with damelaflag string
print("Verifying fake signature")
conn.sendline(b"verify")
conn.recvuntil(b"> ").decode()
conn.sendline(correctSign[:32] + flagCommand.hex())
print(conn.recvuntil(b"> ").decode())