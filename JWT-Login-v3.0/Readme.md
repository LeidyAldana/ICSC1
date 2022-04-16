# JWT Version 3

## Enunciado

Hay un enlace y el archivo ./main.py

En el enlace hay:

Field: Username
CTA: Login

El archivo main.py es un archivo de python, el cual crea un Flask environment

## Solución

En contraste a la versión 2, esta versión tiene un SECRET_KEY de la librería secret de Python (no es generado aleatoriamente como los otros), entonces se descarga un diccionario https://github.com/kaonashi-passwords/Kaonashi de 9GB.

El diccionario se divide en varias partes para que pueda procesarse, quedan partes similares de aproximadamente 914MB.

### Herramienta JWTcat

Pasa a analizarse cada parte del diccionario por la herramienta Jwtcat:
https://github.com/aress31/jwtcat

La cual esta desarrollada en Python para detectar y explotar imperfecciones criptograficas de los JWT, entonces cada una de esas partes, para encontrar la clave con el comando:

python jwtcat.py wordlist -w /home/j7032681/Downloads/kaonashi/xaa "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1lZ2FzZWNyZXQiLCJpc19hZG1pbiI6ZmFsc2UsImlhdCI6MTY0Njg3MDU3NH0.EGB1l6CP3afW0ft5aFuKLVyT7MHl3fgQj6RkloN7S0s"

De lo cual se obtiene que la clave es megasecret, se coloca en jwt.io

### Modificación del JWT

Se cambia la parte de is_admin a True, igual que en la versión 2.

Se acutiliza el token, se recarga la página y se obtiene la flag ^^

### Otras fuentes consultadas

Esta fuente también ayudó:

https://blog.pentesteracademy.com/hacking-jwt-tokens-dictionary-attack-on-symmetric-signing-algorithms-f807dd64f1b5
