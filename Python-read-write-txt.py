
# Criação de arquivos
# leitura e escrita


# criando o arquivo e gravando conteúdo
arch1 = open("arq/arquivo1.txt", "w")
arch1.write("Python é uma Linguagem poderosa")
arch1.close()

# lendo o arquivo e atribuindo a uma variável
arch1 = open("arq/arquivo1.txt", "r")
res = arch1.read() 
print(res)
print("")
arch1.close()

# reescrevendo o conteudo do arquivo
arch2 = open("arq/arquivo1.txt", "w")
arch2.write("Testando gravação de arquivos em Python ")
arch2.close()

# acrescentando conteudo
arch2 = open("arq/arquivo1.txt", "a")
arch2.write("acrescentando conteudo")
arch2.close()

# lendo o arquivo e imprimindo 
arch3 = open("arq/arquivo1.txt", "r")
print(arch3.read())
print("")
