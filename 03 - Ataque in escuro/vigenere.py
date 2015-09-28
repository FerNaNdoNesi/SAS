import itertools

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

def retornaVetorWord(tstTransposicao):
	listCeasar = list(tstTransposicao)
	aux = ''
	vetor = []
	flag = -1
	for x in tstTransposicao:		
		if x != ' ':
			#print 'nao espaco'+ str(aux)
			aux += x 
		else:
			#print 'eh espaco'+ str(aux)
			flag = 0
			vetor.append(aux)
			aux = ''
	#for x in vetor:
	#	print x
	#	print
	if flag == -1:
		return -1
	return vetor

def teste():
	produto = itertools.product('abcd123', repeat=4)

	for chave in produto:
		print "".join(chave)

def vigenereSearchKey_2(textoEscuro, textoDicionario):	
	#print textoDicionario
	#vetorKey = []
	#vetorQtd = []
	indexKey = 0
	indexQtd = 0
	produto = itertools.product('ren24', repeat=5)

	for key in produto:
		print "testando: "+"".join(key)
		contador = 0
		
		tstVigenere = vigenereDecrypt(textoEscuro, "".join(key))
		vetorTexto = retornaVetorWord(tstVigenere)
		vetorDicionario = retornaVetorWord(textoDicionario)		

		if vetorTexto != -1 and vetorDicionario != -1:				
			for y in vetorTexto:
				for z in vetorDicionario:
					if y == z:
						print y+' |igualdade| '+z
						contador += 1
		#vetorKey.append(key)
		#vetorQtd.append(contador)
		if contador > indexQtd:
			indexQtd = contador
			indexKey = key


	print 'Chave encontrada: '+str(indexKey)+' Quantidade palavras iguais: '+str(indexQtd)

	#for c in vetorQtd:
	#	print 'x'+str(c)
	return indexKey
