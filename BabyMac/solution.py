from pwn import *
from binascii import unhexlify


def xor(a, b):
    return bytes(aa ^ bb for aa, bb in zip(a, b))

def pad(data, bsize):
    b = bsize - len(data) % bsize
    return data + bytes([b] * b)

address = ("babymac.sexy-allpacks.com", 10001)

# Crea una conexión al servidor y puerto del enunciado del ejercicio
conn = remote(address[0], address[1])
conn.recvuntil(b"> ").decode()

print("Sign de un string vacio")
conn.sendline(b"sign")
# La siguiente función depende de la librería pwn
# Reciba datos hasta que se encuentre el primer parametri pasado
conn.recvuntil(b"> ")
conn.sendline(b"")
emptySignature = bytes.fromhex(conn.recvuntil(b"> ").decode().split("\n")[0].strip())

print("Sign del string que se necesita")
flagCommand = pad(b"damelaflag", 16)
conn.sendline(b"sign")
# Payload: Primer bloque - all 0x10, segundo bloque - all 0x00, 
# tercer bloque es damelaflag string xored con el sign vacio
payload = b"\x10" * 16 + b"\x00" * 16 + xor(flagCommand, emptySignature)
conn.recvuntil(b"> ").decode()
conn.sendline(payload.hex())
correctSign = conn.recvuntil(b"> ").decode().split("\n")[0]

# Toma el signature del payload y lo envía
# para verificar con el string damelaflag
print("Verifica la firma")
conn.sendline(b"verify")
conn.recvuntil(b"> ").decode()
conn.sendline(correctSign[:32] + flagCommand.hex())
print(conn.recvuntil(b"> ").decode())