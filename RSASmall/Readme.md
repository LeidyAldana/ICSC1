## RSA Small

Insumos:

chall.py
flag.txt.enc
pub.key

Fuente: https://www.youtube.com/watch?v=M-yg0vbrAOk

Procedimiento:

python3 RsaCtfTool.py --publickey /home/k7032681/Downloads/hack/rsasmall/pub.key --uncipherfile /home/k7032681/Downloads/hack/rsasmall/flag.txt.enc

Unciphered data :
HEX : 0x00000000464c41477b536d616c6c5072696d657356756c6e7d
INT (big endian) : 102740453687121646714848423017668071274062564585085
INT (little endian) : 787345297321404882610670702314605839848553648356058988544000
utf-8 : FLAG{SmallPrimesVuln}
STR : b'\x00\x00\x00\x00FLAG{SmallPrimesVuln}'


