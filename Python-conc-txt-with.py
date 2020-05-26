# Pacotes
# funções Built-in
# leitura e gravação de arquivo
# comando with

# impportar o pacote OS
import os

# definindo a cadeia de caracteres
texto = "Aprender Python para formação "
texto += 'em ciência de dados.' # concatenação de strings

# criando um arquivo e gravando a cadeia de caracteres 
newfile = os.path.join('arq/cientista.txt') # cria um novo arquivo .txt
arq1 = open(newfile, 'w')
arq1.write(texto) # gravando os caracteres no arquivo
arq1.close()

# lendo o arquivo gravado
arq1 = open('arq/cientista.txt', 'r')
conteudo = arq1.read()
arq1.close()

print(conteudo)
print("")

# usando o comando with
with open('arq/cientista.txt', 'r') as arch:
	conteudo = arch.read()

print(conteudo)
print("")
