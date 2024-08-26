from requests import *

HEADER = '\033[95m'
blue = '\033[94m'
OKCYAN = '\033[96m'
green = '\033[92m'
erro = '\033[93m'
falha = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
white = '\033[97m'
UNDERLINE = '\033[4m'

def pesquisarSubdominios(url, listSub):
        print(white+'\nEscaneando {}...'.format(url))
        for sub in listSub:
                try:
                        requisicao = get('https://'+sub.strip()+'.'+url)
                        if(requisicao.status_code >=200 and requisicao.status_code < 300):
                                print(green+'[*]https://'+sub.strip()+'.'+url+': '+str(requisicao.status_code)+white)
                        #else:
                               #print(erro+'[*]https://'+sub.strip()+'.'+url+': '+str(requisicao.status_code))
                except:
                        #print(falha+'https://'+sub.strip()+'.'+url+': ERRO NO SUBDOMINIO!'+white)
                        continue

def pesquisarDiretorios(url1, listDir):
        print(white+'\nEscaneando {}...'.format(url1))
        for dir in listDir:
                try:
                        if(url1[len(url1)-1] == '/'):
                            requisicao = get(url1+dir.strip())
                            if(requisicao.status_code >= 200 and requisicao.status_code < 300):
                                print(green+'[*]'+url1+dir.strip()+': '+str(requisicao.status_code)+white)
                        else:
                              requisicao = get(url1+'/'+dir.strip())
                              if(requisicao.status_code >= 200 and requisicao.status_code < 300):
                                print(green+'[*]'+url1+'/'+dir.strip()+': '+str(requisicao.status_code)+white)
                    #else:
                            #print(erro+'[*]'+url1+'/'+dir.strip()+': '+str(requisicao.status_code))
                except:
                        print(falha+'ERRO! VERIFIQUE A SUA CONEXAO A INTERNET.'+white)

print('Para escanear diretorios: https://exemplo.com')
print('Para escanera subdominios: exemplo.com')

file1 = open('wordlistDeSubdominio.txt','r')#change file name!
file2 = open('wordlistDeDiretorios.txt','r')#change file name!

pesquisarSubdominios('example.com', file1)#cahnge url address!
pesquisarDiretorios('https://example.com/', file2)#cahnge url address!
