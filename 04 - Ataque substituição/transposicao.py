import time
import struct
import os
import math

def monta_matriz_Normal(conteudo, key):
	count = 0
	tamanho = len(conteudo)	
	linha = int(math.ceil(float(tamanho)/float(key)))
	coluna = key
	
	# Criando matriz
	matriz = []
	for l in range(linha):      
		linha = []
		for c in range(coluna):			
			if(count > (len(conteudo)-1)): 
				campo = ' '
				linha = linha + [campo]
			else:
				campo = conteudo[count]
				linha = linha + [campo]
			count += 1

		matriz = matriz + [linha]
	return matriz

def monta_matriz_Transp(conteudo, key):
	count = 0
	tamanho = len(conteudo)	
	coluna = int(math.ceil(float(tamanho)/float(key)))
	linha = key
	
	# Criando matriz
	matriz = []
	for l in range(linha):      
		linha = []
		for c in range(coluna):			
			if(count > (len(conteudo)-1)): 
				campo = ' '
				linha = linha + [campo]
			else:
				campo = conteudo[count]
				linha = linha + [campo]
			count += 1

		matriz = matriz + [linha]
	return matriz

def MatrizTransposta(matriz):
	matrizRetorno=[]
	for j in range(len(matriz[0])):
		linha=[]
		for i in range(len(matriz)):
			linha.append(matriz[i][j])
		matrizRetorno.append(linha)
	return matrizRetorno

def printMatrix(matrix):
	text_decrypt = ''
	#print matrix
	for i, element in enumerate(matrix):
		text_decrypt = text_decrypt+''.join(element)
	return text_decrypt

def transposicaoEncrypt(conteudo, key):
	matriz = monta_matriz_Normal(conteudo, key)
	Tmatriz = MatrizTransposta(matriz)
	
	return printMatrix(Tmatriz)

def transposicaoDecrypt(conteudo, key):	
	matriz = monta_matriz_Transp(conteudo, key)	
	Tmatriz = MatrizTransposta(matriz)	
	
	return printMatrix(Tmatriz)

def transposicaoSearchKey(textoClaro, textoEscuro):	
	for x in xrange (2,200):
		key = x
		tstTransposicao = transposicaoDecrypt(textoEscuro, key)
		if(textoClaro == tstTransposicao):			
			return key
	return 0

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

def transposicaoSearchKey_2(textoEscuro, textoDicionario):	
	#print textoDicionario
	#vetorKey = []
	#vetorQtd = []
	indexKey = 0
	indexQtd = 0
	for x in xrange (10,30):
		contador = 0
		key = x
		tstTransposicao = transposicaoDecrypt(textoEscuro, key)
		vetorTexto = retornaVetorWord(tstTransposicao)
		vetorDicionario = retornaVetorWord(textoDicionario)		

		if vetorTexto != -1 and vetorDicionario != -1:				
			for y in vetorTexto:
				for z in vetorDicionario:
					if y == z:
						#print y+' |igualdade| '+z
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