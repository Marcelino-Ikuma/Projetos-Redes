import socket

green = '\033[92m'
falha = '\033[93m'
erro = '\033[91m'
white = '\033[97m'

def verificarPortas(host, portaInicio, portaFinal):
    print('Escanendo {}...'.format(host))
    portasAbertas = 0
    for porta in range(portaInicio, portaFinal + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            conexao = sock.connect_ex((host, porta))
            if(conexao == 0):
                servico = socket.getservbyport(porta)
                print(green+'Porta {} esta aberta. Serviço: {}'.format(porta, servico)+white)
                portasAbertas = portasAbertas + 1
           # else:
                #print(erro+'Porta {} esta fechada.'.format(porta)+white)
        except:
            print(erro+'Erro de conexao!'+white)
            continue

    print('{} porta(s) abertas no intervalo de {} a {}'.format(portasAbertas, portaInicio, portaFinal))

def verificarPortaEspecifica(host, porta):
    print('Escaneando {}...'.format(host))
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        conexao = sock.connect_ex((host, porta))
        if(conexao == 0):
            servico = socket.getservbyport(porta)
            print(green+'Porta {} esta aberta. Servico: {}'.format(porta, servico)+white)
        else:
            print(falha+'Porta {} esta fechada.'.format(porta)+white)
    except:
        print(erro+'Problema de conexao. Por favor verifique a sua conexao a internet!'+white)

print('Exemplo de alvo: exemplo.com')
alvo = input('Digite o alvo a ser escaneado: ')
inicio = int(input('Digite a porta de incio: '))
fim = int(input('Digite a porta final: '))

verificarPortas(alvo, inicio, fim)
#Pode tirar a linha de baixo como comentário para fazer o scan de uma só porta, nao esqueca de alterar a porta a ser scaneada
#verificarPortaEspecifica(alvo, 80)
