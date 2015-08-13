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

#minhas bibliotecas#
import ceasar
import transposicao
import vigenere
#minhas bibliotecas#

def lerEntrada(nomeArq):
	arquivo = open(nomeArq, "rb")
	conteudo = arquivo.read()	
	return conteudo


def gravarArquivo(conteudo, nomeArq):
	arquivo = open(nomeArq, 'wb')
	arquivo.seek(0)
	arquivo.write(conteudo)
	arquivo.close()
############################# INICIO SISTEMA #############################

print 'Inicializado...'

conteudoOriginal = lerEntrada("inputs/entrada.txt")
chaveNum = 3
chaveStr = 'chave'


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
gravarArquivo(vigenereDecrypt, 'outputs/05 - vigenereDecrypt.txt')