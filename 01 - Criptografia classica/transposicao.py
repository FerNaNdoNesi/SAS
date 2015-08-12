import time
import struct
import os
import math

def monta_matriz(conteudo, key):
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

def transposta(matriz):
	matrizRetorno=[]
	for j in range(len(matriz[0])):
		linha=[]
		for i in range(len(matriz)):
			linha.append(matriz[i][j])
		matrizRetorno.append(linha)
	return matrizRetorno

def printMatrix(matrix):
	text_decrypt = ''
	for i, element in enumerate(matrix):
		#print ''.join(element)
		text_decrypt = text_decrypt+''.join(element)
	return text_decrypt

def transposicaoEncrypt(conteudo, key):
	matriz = monta_matriz(conteudo, key)	
	Tmatriz = transposta(matriz)
	
	return printMatrix(Tmatriz)

def transposicaoDecrypt(conteudo, key):
	matriz = monta_matriz(conteudo, key)	
	Tmatriz = transposta(matriz)
	
	return printMatrix(Tmatriz)