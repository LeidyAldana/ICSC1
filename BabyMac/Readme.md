# Baby MAC

https://0awawa0.medium.com/dragon-ctf-2021-baby-mac-writeup-b7cb8ca3f95a

## Enunciado

    We implemented a simple signing service. Can you sign a flag request?

    nc babymac.sexy-allpacks.com 10001

    Y esta el archivo analyzed.py

## Solución

En el archivo analyzed.py hay dos operaciones:

Sign, Verify

Las cuales por operaciones bit a bit (en números binarios) determinan si mostrar la Flag o no. La llave de estas operaciones es generada aleatoriamente en cada nueva conexión (ver los comentarios en el código).

### ¿Qué es la operación XOR?

Esta operación tiene como resultado 1 cuando las entradas son diferentes:

0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0

### ¿Qué es AES?

Advanced Encryption Standard, es un algoritmo de cifrado por bloques simétrico.


### ¿Cómo incluir el string 'damelaflag' en data?

El string necesita estar solo en el último bucle (líneas 33 a 36) y la primera parte de esa cadena puede ir vacio para determinar la variable mac, entonces se escribe el script solution.py

### Fuentes de información 

https://0awawa0.medium.com/dragon-ctf-2021-baby-mac-writeup-b7cb8ca3f95a

https://www.trentonsystems.com/blog/aes-encryption-your-faqs-answered