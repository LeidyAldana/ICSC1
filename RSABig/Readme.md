## RSA Big

Insumos:

chall.py
flag.txt.enc
pub.key

Fuente: https://www.youtube.com/watch?v=M-yg0vbrAOk

Procedimiento:

python3 RsaCtfTool.py --publickey /home/k7032681/Downloads/hack/rsabig/pub.key --uncipherfile /home/k7032681/Downloads/hack/rsabig/flag.txt.enc

Unciphered data :
HEX : 0x464c41477b5573696e675f536d616c6c5f655f49735f496e7365637572657d
INT (big endian) : 124205587181285638501078536535932639734638373844260981480300633467984700797
INT (little endian) : 221556045274671331641659985701093936947456036900879358921738112550851136582
utf-8 : FLAG{Using_Small_e_Is_Insecure}
STR : b'FLAG{Using_Small_e_Is_Insecure}'


