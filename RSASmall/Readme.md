## RSA Small

## Enunciado

Esta la siguiente pregunta:

Hice un programa para cifrar mi flag pero olvidé guardar la llave privada ¿Me ayudas a descifrar el flag?

Y un archivo .zip que contiene los siguientes archivos:

chall.py --> Algoritmo
flag.txt.enc --> Flag encriptada
pub.key --> Llave pública


## Solución

En el archivo chall.py se observa que el algoritmo de cifrado es RSA (Rivest-Shamir-Adleman) el cual es un algoritmo asimetrico, es decir, que utiliza dos llaves, una pública y una privada.

### ¿Cómo funciona el algoritmo?

Funciona gracias a la operación matemática módulo, en la siguiente ruta puede verse detalladamente el algoritmo y un ejemplo del funcionamiento del mismo:

https://hackernoon.com/how-does-rsa-work-f44918df914b

### Procedimiento

Se utilizó la herramienta RSACtfTool, la cual recupera la llave privada del algoritmo RSA con varios ataques:

https://github.com/Ganapati/RsaCtfTool

Después de leer la documentación, se pasa al script la llave pública y el texto encriptado:

python3 RsaCtfTool.py --publickey /home/k7032681/Downloads/hack/rsasmall/pub.key --uncipherfile /home/k7032681/Downloads/hack/rsasmall/flag.txt.enc

Se obtiene la siguiente salida, entre lo cual está la Flag:

Unciphered data :
HEX : 0x00000000464c41477b536d616c6c5072696d657356756c6e7d
INT (big endian) : 102740453687121646714848423017668071274062564585085
INT (little endian) : 787345297321404882610670702314605839848553648356058988544000
utf-8 : FLAG{SmallPrimesVuln}
STR : b'\x00\x00\x00\x00FLAG{SmallPrimesVuln}'



### Otras fuentes consultadas

https://int0x33.medium.com/day-18-essential-ctf-tools-1f9af1552214

### Otros items

Es posible que el script de Python necesite instalar dependencias, como sage para procedimientos matemáticos.