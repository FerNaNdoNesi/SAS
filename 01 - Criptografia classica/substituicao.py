import time
import struct
import os
import math
import random

def random_not_repeat(conteudo):	
	count = 0
	myList = list(xrange(256))	
	num_random = []
	random.shuffle(myList)
	
	# Criando matriz
	matriz = []
	for l in range(len(conteudo)):      
		linha = []
		for c in range(2):			
			if(c == 0): 
				if(count > (len(conteudo)-1)): 
					campo = ' '
				else:
					campo = conteudo[l]

				linha = linha + [campo]
				count += 1
			else:
				campo = myList.pop()
				linha = linha + [campo]			

		matriz = matriz + [linha]		
	return matriz

def printMatrix(matrix):
	text_decrypt = ''
	#print matrix
	for i, element in enumerate(matrix):
		text_decrypt = text_decrypt+''.join(str(element))
	return text_decrypt

def substituicaoEncrypt(matriz, size):
	matrizRetorno=[]
	for i in range(size):
		linha=[]		
		for j in range(2):
			if(j == 1):
				linha.append(matriz[i][j])
		matrizRetorno.append(linha)		
	return matrizRetorno

def substituicaoDecrypt(matriz_original, matriz_crip):
	result = ''	
	for i in range(len(matriz_crip)):
		linha=[]		
		for j in range(2):
			if(j == 1):				
				result = result + matriz_original[i][j-1]
	return result	