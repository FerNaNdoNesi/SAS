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

def ceasarSearchKey(textoClaro, textoEscuro):
	vlrCla = ord(textoClaro[0])
	vlrEsc = ord(textoEscuro[0])
	key = (vlrEsc - vlrCla)%256
 
	tstCesar = ceasarEncrypt(textoClaro,key)

	if(tstCesar == textoEscuro):		
		return key
	else:
		return 0

def retornaVetorWord(tstCeasar):
	listCeasar = list(tstCeasar)
	aux = ''
	vetor = []
	flag = -1
	for x in tstCeasar:		
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
			

def ceasarSearchKey_2(textoEscuro, textoDicionario):	
	for x in xrange (20,22):
		key = x
		tstCeasar = ceasarDecrypt(textoEscuro, key)
		vetorTexto = retornaVetorWord(tstCeasar)
		vetorDicionario = retornaVetorWord(textoDicionario)		
		
		if vetorTexto != -1:	
			print 'gggg'+str(vetorTexto[0])
			for y in vetorTexto:
				for z in vetorDicionario:
					if y == z:
						print y+' |igualdade| '+z



	print 'retorno'+str(key)
	return 0