'''
Esse programa serve para converter um texto normal
em hash MD5, SHA-256 e SHA-512
'''

from hashlib import *
from os import system

system('cls')

escolha_hash = 0
texto_claro = input('Digite alguma coisa um texto ou palavra a ser transformada em hash: ')

while(escolha_hash != '1' and escolha_hash != '2' and escolha_hash != '3'):
    escolha_hash = input('Escolhe o tipo de hash: \n[1] MD5\n[2] SHA-256\n[3] SHA-512\n')

print('Texto Claro: {}'.format(texto_claro))
if(escolha_hash == '1'):
    texto_hash = md5(texto_claro.encode()).hexdigest()
    print('Texto Md5: {}'.format(texto_hash))
elif(escolha_hash == '2'):
    texto_hash= sha256(texto_claro.encode()).hexdigest()
    print('Texto SHA-256: {}'.format(texto_hash))
else:
    texto_hash = sha512(texto_claro.encode()).hexdigest()
    print('Texto SHA-512: {}'.format(texto_hash))
