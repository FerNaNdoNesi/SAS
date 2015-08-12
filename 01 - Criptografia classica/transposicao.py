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
			campo = conteudo[count]
			count += 1
			linha = linha + [campo]
			if(count > (len(conteudo)-1)): 
				break

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

def mostra_matriz(matriz, conteudo):
	count = 0
	print 'Matriz'     
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):            
			print matriz[i][j]
			if(count == (len(conteudo)-1)): # para nao dar erro de indexacao
				return;
			count += 1
		print
	print

def transposicaoEncrypt(conteudo, key):
	matriz = monta_matriz(conteudo, key)
	#print matriz
	#Tmatriz = transposta(matriz)



	return str(matriz)