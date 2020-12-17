cont_nome = 1 #contador para abrir todos os arquivos .in
nome = "arq" + str(cont_nome) + ".in" #nome do arquivo a ser aberto
cont = 0 #contador para descobrir quantas palavras procurar
n = 0 #numero de palavras a serem procuradas
lista = [] #diagrama
palavras = [] #palavras a serem achadas
arq = open(nome, "r") #abrindo o arquivo
conte = arq.read().split("\n") #adicionando o arquivo a uma variavel
arq.close() #fechando o arquivo
while not conte[cont].isdigit():
	lista.append(conte[cont].split(" "))
	cont += 1
if conte[cont].isdigit():
	n = int(conte[cont])
for j in range(cont+1, len(conte)):
	palavras.append(conte[j])

d = [["." for i in range(len(lista[0]))] for j in range(len(lista))]

for i in range(len(lista)):
	print(lista[i])
for i in range(len(d)):
	print(d[i])
	

for i in range(len(palavras)):
	for j in range(len(palavras[i])):
		for x in range(len(lista)):
			for y in range(len(lista[x])):
				if palavras[i][j] == lista[x][y]:
					del d[x][y]
					d.insert(([x][y]), palavras[i][j])
	
