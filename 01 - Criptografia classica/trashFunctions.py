def cifraCeasar_encrypt(conteudo, key):
	tamanho = len(conteudo)
	splited = []
	for x in xrange(1,tamanho):
		splited.append[x]

	cifrado = ''
	for x in xrange(1,tamanho):		
		print conteudo[x] #,'@'
		cifrado[x] = chr((ord(conteudo[x])+key)%256)		

	return cifrado

def encrypt(text, key): #http://www.geeksbr.com/2013/12/python-implementacao-da-cifra-de-cesar.html
	text_list = list(text)
	text_encrypt = ""
	for i in text_list:
		
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				ord_c = (ord(i) - ord('a') + key) % 26
				text_encrypt += chr(ord_c + ord('a'))
			else:
				ord_c = (ord(i) - ord('A') + key) % 26
				text_encrypt += chr(ord_c + ord('A'))
		else:
			text_encrypt += i
	return text_encrypt

def decrypt(text, key): #http://www.geeksbr.com/2013/12/python-implementacao-da-cifra-de-cesar.html
	text_list = list(text)
	text_encrypt = ""
	for i in text_list:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			if (i >= 'a' and i <= 'z'):
				ord_c = (ord(i) - ord('a') - key) % 26
				text_encrypt += chr(ord_c + ord('a'))
			else:
				ord_c = (ord(i) - ord('A') - key) % 26
				text_encrypt += chr(ord_c + ord('A'))
		else:
			text_encrypt += i
	return text_encrypt