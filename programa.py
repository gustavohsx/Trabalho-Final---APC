cont_nome = 1 #contador para abrir os arquivos externos
nome = "arq" + str(cont_nome) + ".in" #nome do arquivo externo
cont = 0 #contador de linhas do conteudo externo
n = 0 #numero de palavras a serem procuradas
diagrama = [] #diagrama
palavras = [] #palavras a serem achadas
arq = open(nome, "r") #abrindo o arquivo externo
conte = arq.read().split("\n") #adicionando o arquivo a uma variavel
arq.close() #fechando o arquivo

while not conte[cont].isdigit():
	diagrama.append(conte[cont].split(" ")) #adicionando o diagrama a variavel diagrama
	cont += 1
if conte[cont].isdigit():
	n = int(conte[cont]) #adicionando o numero de palavras
for j in range(cont+1, len(conte)):
	palavras.append(conte[j]) #adicionando as palavras a serem achadas a variavel palavras

d = [["." for i in range(len(diagrama[0]))] for j in range(len(diagrama))] #criando o diagrama final

for i in range(len(diagrama)):
	print(diagrama[i])

lista=[]

def encontrarPalavras():
	for palavra in palavras:
	
		for x in range(len(diagrama)):
			for y in range(len(diagrama[x])):
				for i in range(len(palavra)):
					if diagrama[x][y] == palavra[i]:
						a = diagrama[x][y] + ' ' + str(x) + ' ' + str(y)
						lista.append(a.split(' '))
						d[x][y] = diagrama[x][y]

def exibirDiagramaFinal():
	print(' - ' * 15)
	for i in range(len(d)):
		print(d[i])

encontrarPalavras()
exibirDiagramaFinal()
