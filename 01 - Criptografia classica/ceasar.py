def ceasarEncrypt(conteudo, key):
	text_encrypt = ""
	for x in conteudo:
		ord_c = (ord(x) + key) % 256
		text_encrypt += chr(ord_c)
	return text_encrypt

def ceasarDecrypt(conteudo, key):
	text_decrypt = ""
	for x in conteudo:
		ord_c = (ord(x) - key) % 256
		text_decrypt += chr(ord_c)
	return text_decrypt