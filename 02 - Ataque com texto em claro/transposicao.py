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