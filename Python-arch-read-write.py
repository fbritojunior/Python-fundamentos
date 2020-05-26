
# Automatizando o processo de gravação
# funções built-in
# função Input
# manipulação de strings
# lendo e escrevendo em um arquivo

# entrando com o nome do arquivo
filename = input("Digite o nome do arquivo:")
filename = filename + '.txt' # concatenação de strings

# abrindo e granvando no arquivo
arq1 = open(filename, 'w')
arq1.write("Inclusão de texto no arquivo.")
arq1.close()

# lendo o arquivo gravado e imprimindo
arq1 = open(filename, 'r')
print(arq1.read())
arq1.close()