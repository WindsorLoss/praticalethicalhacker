import sys
import socket as sk
from datetime import datetime as dt

#Definir nosso alvo
if len(sys.argv) == 2: # Verifica se foram passados 2 argumentos ao chamar o programa. Ex.: python3 portscanner.py <ip>
    target = sk.gethostbyname(sys.argv[1]) #Traduz o hostname para IPv4

    #Adicionando um banner
    print('-' * 50)
    print(f'Escaneando alvo: {target}')
    print(f'Início da execução: {dt.now()}')
    print('-' * 50)

    try:
        for port in range(50,85):
            s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
            sk.setdefaulttimeout(1) #Caso não consiga conectar de cara, se desconecta em um segundo
            result = s.connect_ex((target, port)) #Verifica se uma porta está aberta. Se estiver, retorna 0, senão retorna 1
            #O connect_ex é chamado de "air indicator", pelo motivo descrito no cometário anterior
            if result == 0:
                print(f'Porta {port} está aberta!')
            s.close()

        print('-' * 50)
        print('Scan completo!')
        print(f'Fim da execução: {dt.now()}')
        print('-' * 50)

    except KeyboardInterrupt: #Interrompe o programa em caso de um CTRL+C
        print('\nSaindo do programa...')
        sys.exit()
    
    except sk.gaierror:
        print('\nNão foi possível resolver o nome do host.')
        sys.exit()

    except sk.error:
        print('\nNão foi possível se conectar ao servidor.')
        sys.exit()

else:
    print('Quantidade de argumentos inválida')
    print('Sintaxe: python3 portscanner.py <IP>')



