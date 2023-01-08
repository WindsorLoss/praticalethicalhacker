meses = open('..\\meses.txt') #Modo leitura
print(meses.read()) #Lê todo arquivo de uma vez
#É possível passar .readline() para ler só uma linha, ou .readlines() para várias

dias = open('..\\dias.txt', 'w') #Modo de escrita. Cria um arquivo caso não exista
dias.write('Segunda') #Neste modo, ele irá sobrescrever o arquivo, e não adicionar um texto a mais

dias = open('..\\dias.txt', 'a') #Modo append. Adiciona novo texto ao invés de sobrescrever o existente
dias.write('\nTerça')

dias = open('..\\dias.txt') #Trocando para o modo leitura
print('\n'+dias.read())

meses.close()
dias.close()

