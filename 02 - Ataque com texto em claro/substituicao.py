import time
import struct
import os
import math
import random

def cria_mapeamento(conteudoClaro, conteudoEscuro):	
	ListaClara  = list(conteudoClaro)
	ListaEscura = list(conteudoEscuro)
	#
	mapeamento = []
	for x in range(len(ListaClara)):
	    mapeamento.append(ListaClara[x])
	    mapeamento.append(ListaEscura[x])
	#    
	return mapeamento		

def substituicaoDecrypt(conteudoEscuro, mapeamento):	
	count  = 0
	result = ''	
	for i in mapeamento:				
		if(count%2 == 0): # conteudo claro -> posicao '0' e 'PAR' na lista
			result += mapeamento[count]
		count += 1		
	
	return str(result)

def substituicaoEncrypt(conteudoEscuro, mapeamento):	
	count  = 0
	result = ''	
	for i in mapeamento:				
		if(count%2 != 0): # conteudo escuro -> posicao 'IMPAR' na lista
			result += mapeamento[count]
		count += 1		
	
	return str(result)	