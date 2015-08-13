def vigenereEncrypt(conteudo, key):
	text_encrypt = ""
	tConteudo = len(conteudo)
	tChave = len(key)
	cont=0

	for x in conteudo:
		ord_c = (ord(x) + ord(key[cont])) % 256
		text_encrypt += chr(ord_c)
		if cont >= tChave-1:
			cont = 0
		else:
			cont += 1

	return text_encrypt

def vigenereDecrypt(conteudo, key):
	text_encrypt = ""
	tConteudo = len(conteudo)
	tChave = len(key)
	cont=0

	for x in conteudo:
		ord_c = (ord(x) - ord(key[cont])) % 256
		text_encrypt += chr(ord_c)
		if cont >= tChave-1:
			cont = 0
		else:
			cont += 1

	return text_encrypt