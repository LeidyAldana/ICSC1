## RSA Big

## Enunciado

Esta el siguiente texto:

Mi programa ahora es más seguro ¡Ya no podrás descifrar mi flag!

Y un archivo .zip que contiene los siguientes archivos:

chall.py --> Algoritmo
flag.txt.enc --> Flag encriptada
pub.key --> Llave pública


## Solución

En el archivo chall.py se observa que el algoritmo de cifrado es RSA (Rivest-Shamir-Adleman), donde la primera versión (RSA Small) utilizada la librería Crypto.Util.number de Python en su función getPrime(100), en contraste, RSA Big tiene getPrime(4096)

### Procedimiento

Este caso cambia en el tamaño de los valores p y q, por tal toma más tiempo su procesamiento al recuperar la llave privada del algoritmo RSA con varios ataques:

python3 RsaCtfTool.py --publickey /home/k7032681/Downloads/hack/rsabig/pub.key --uncipherfile /home/k7032681/Downloads/hack/rsabig/flag.txt.enc


Se obtiene la siguiente salida, entre lo cual está la Flag:

Unciphered data :
HEX : 0x464c41477b5573696e675f536d616c6c5f655f49735f496e7365637572657d
INT (big endian) : 124205587181285638501078536535932639734638373844260981480300633467984700797
INT (little endian) : 221556045274671331641659985701093936947456036900879358921738112550851136582
utf-8 : FLAG{Using_Small_e_Is_Insecure}
STR : b'FLAG{Using_Small_e_Is_Insecure}'


