from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
from Crypto.PublicKey import RSA

p = getPrime(100)
q = getPrime(100)
n = p*q
e = 65537

#rsakey = RSA.construct((1022019600781309348633170917009891556341356135103199142819997,e))
#print(rsakey)

n = 1022019600781309348633170917009891556341356135103199142819997

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a


def ncf(num):   
    cont = 0 
    for i in range(num):
        tmp = gcd(i+1,num)
        if tmp>1:
            pass
        else:
            cont = cont + 1
        print('pPara '+str(i+1)+' con n '+str(num)+' conts: '+str(cont)+' tmp: '+str(tmp))

ncf(int(n))

#d = modinv(e, n-(p+q-1))

#key = RSA.construct((n, int(e), p, d, q))



#print(signer)


## No sé si funciona
#with open('pub.key', 'r') as fd: #wb
    #fd.write(rsakey.export_key())


# with open('flag.txt.enc', 'r') as fd:
  # ciphertext = long_to_bytes(pow(bytes_to_long(fd.read()), d, n))
  # print('Ciphertext:')
  # print(ciphertext)
   #fd.write(ciphertext)
