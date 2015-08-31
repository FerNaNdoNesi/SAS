# Desenvolver um programa com 4 tipos de criptografia classica
# 1 - Cifra de ceasar
# 2 - Cifra de Transposicao
# 3 - Cifra de Vigenere
# 4 - Cifra de Substituicao

def clear(): # LIMPANDO A TELA
	import curses
	import termios
	from sys import stdin
	fd = stdin.fileno()
	scr = termios.tcgetattr(fd)
	scrn = curses.initscr()
	scrn.clear()
	termios.tcsetattr(fd, termios.TCSADRAIN, scr)

import time
import struct
import os
import math
import random

#minhas bibliotecas#
import ceasar
import transposicao
import vigenere
import substituicao
#minhas bibliotecas#

def lerEntrada(nomeArq):
	arquivo = open(nomeArq, "rb")		
	conteudo = arquivo.read()	
	arquivo.close()
	return conteudo

def gravarArquivo(conteudo, nomeArq):
	arquivo = open(nomeArq, 'wb')
	arquivo.seek(0)
	arquivo.write(conteudo)
	arquivo.close()

# Testa se o texto descriptografado eh igual ao texto original
def testa_igualdade(conteudoOriginal, conteudoDescriptografado):	
	for i in range(len(conteudoOriginal)):
		if(conteudoOriginal[i] != conteudoDescriptografado[i]):
			return 'O texto descriptografado nao eh igual ao texto original!'
	return 'O texto descriptografado eh igual ao texto original!'

def T1_Encrypt():
	conteudoOriginal = lerEntrada("inputs/entrada.txt")
	chaveNum = 21
	chaveStr = 'ChaveDeTeste'

	print 'Encryptando Ceasar... (gravado) key = '+str(chaveNum)
	ceasarEncrypt = ceasar.ceasarEncrypt(conteudoOriginal, chaveNum)
	gravarArquivo(ceasarEncrypt, 'outputs/01 - ceasarEncrypt.txt')

	print 'Decryptando Ceasar... (gravado) key = '+str(chaveNum)
	ceasarDecrypt = ceasar.ceasarDecrypt(ceasarEncrypt, chaveNum)
	gravarArquivo(ceasarDecrypt, 'outputs/02 - ceasarDecrypt.txt')

	print 'Encryptando Transposicao... (gravado) key = '+str(chaveNum)
	transposicaoEncrypt = transposicao.transposicaoEncrypt(conteudoOriginal, chaveNum)
	gravarArquivo(transposicaoEncrypt, 'outputs/03 - transposicaoEncrypt.txt')

	print 'Decryptando Transposicao... (gravado) key = '+str(chaveNum)
	transposicaoDecrypt = transposicao.transposicaoDecrypt(transposicaoEncrypt, chaveNum)
	gravarArquivo(transposicaoDecrypt, 'outputs/04 - transposicaoDecrypt.txt')

	print 'Encryptando Vigenere... (gravado) key = '+chaveStr
	vigenereEncrypt = vigenere.vigenereEncrypt(conteudoOriginal, chaveStr)
	gravarArquivo(vigenereEncrypt, 'outputs/05 - vigenereEncrypt.txt')

	print 'Decryptando Vigenere... (gravado) key = '+chaveStr
	vigenereDecrypt = vigenere.vigenereDecrypt(vigenereEncrypt, chaveStr)
	gravarArquivo(vigenereDecrypt, 'outputs/06 - vigenereDecrypt.txt')

	#mat_rand = substituicao.random_not_repeat(conteudoOriginal)
	#gravarArquivo(''.join(str(mat_rand)), 'outputs/09 - matRandom.txt')

	#print 'Encryptando Substituicao... (gravado)'
	#matrizCrip = substituicao.substituicaoEncrypt(mat_rand, len(conteudoOriginal))
	#gravarArquivo(''.join(str(matrizCrip)), 'outputs/07 - substituicaoEncrypt.txt')

	#print 'Decryptando Substituicao... (gravado)'
	#textDescrip = substituicao.substituicaoDecrypt(mat_rand, matrizCrip)
	#gravarArquivo(textDescrip, 'outputs/08 - substituicaoDecrypt.txt')

def T2_SearchKey():

	print '1 Ceasar'
	print '2 Transposicao'
	print '3 Vigenere'
	print '4 Substituicao'
	tipo = int(raw_input())

	if tipo == 1:
		print'Teste Ceasar'
		conteudoEscuro = lerEntrada("outputs/01 - ceasarEncrypt.txt")		
		conteudoClaro = lerEntrada("outputs/02 - ceasarDecrypt.txt")
		#conteudoEscuro = lerEntrada("professor/outputs/pg76.txt.enc")
		#conteudoClaro = lerEntrada("professor/inputs/pg76.txt")
		key = ceasar.ceasarSearchKey(conteudoClaro, conteudoEscuro)
		if key != 0:
			print("Descoberto cifra de ceasar | Key = "+str(key))
	if tipo == 2:
		print'Teste Transposicao'
		conteudoEscuro = lerEntrada("outputs/03 - transposicaoEncrypt.txt")
		conteudoClaro = lerEntrada("outputs/04 - transposicaoDecrypt.txt")		
		#conteudoEscuro = lerEntrada("professor/outputs/pg76.txt.enc")
		#conteudoClaro = lerEntrada("professor/inputs/pg76.txt")
		key = transposicao.transposicaoSearchKey(conteudoClaro, conteudoEscuro)
		if key != 0:
			print("Descoberto cifra de transposicao | Key = "+str(key))
	if tipo == 3:
		print'Teste Vigenere'
		conteudoEscuro = lerEntrada("outputs/05 - vigenereEncrypt.txt")
		conteudoClaro = lerEntrada("outputs/06 - vigenereDecrypt.txt")
		#conteudoEscuro = lerEntrada("professor/outputs/pg76.txt.enc")
		#conteudoClaro = lerEntrada("professor/inputs/pg76.txt")
		key = vigenere.vigenereSearchKey(conteudoClaro, conteudoEscuro)
		if key != 0:
			print("Descoberto cifre de vigenere | Key = "+str(key))
	if tipo == 4:
		print'Teste Substituicao'
		conteudoClaro  = lerEntrada("inputs/pg1342.txt")
		conteudoEscuro = lerEntrada("outputs/pg1342.txt.enc")	
		mapeamento = substituicao.cria_mapeamento(conteudoClaro, conteudoEscuro)	
		# grava o mapeamento...
		gravarArquivo(''.join(str(mapeamento)), 'outputs/mapeamentoSubs.txt')
		# descriptografa para testar a chave de mapeamento..
		textoLimpo = substituicao.substituicaoDecrypt(conteudoEscuro, mapeamento)
		# Testa se o texto descriptografado eh igual ao texto original
		resultado = testa_igualdade(conteudoClaro, textoLimpo)
		print resultado	

############################# INICIO SISTEMA #############################

print 'Inicializado...'

#T1_Encrypt()
T2_SearchKey()