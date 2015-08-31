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


def createKey(key, texto):	
	if len(key) < len(texto):
		mult = len(texto)/len(key)
		modi = len(texto)%len(key)
		lista = list()
		for i in range(0, mult):
			lista.append(key)
		lista.append(key[:modi])
		newKey = ''.join(lista)
		return newKey
	return key


def vigenereSearchKey(textoClaro, textoEscuro):
	chave_compl = vigenereSearchKey_completa(textoClaro, textoEscuro)
	#print chave_compl

	key = ''
	i=0
	for x in xrange (0,200):
		
		ord_c = ord(chave_compl[i])
		key += chr(ord_c)
		chave_completa = createKey(key , textoClaro)
		if(chave_compl == chave_completa):			
			return key
		i += 1
	return 0

def vigenereSearchKey_completa(textoClaro, textoEscuro):
	chave_com = ''
	i = 0
	for x in textoClaro:
		ord_ch = (ord(textoEscuro[i]) - ord(textoClaro[i]))%256
		chave_com += chr(ord_ch)
		i +=1
	return chave_com
