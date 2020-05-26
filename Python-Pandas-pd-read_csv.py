
# pacote Pandas 
# leitura de arquivos .csv com Pandas
# funções Built-in

# importando pacotes
import pandas as pd 

# lendo o primeiro arquivo e imprimindo o cabeçalho
file1 = 'arq/binary.csv' 
arq1 = pd.read_csv(file1)
print(arq1.head())
print("")

# lendo o segundo arquivo e imprimindo 
file2 = 'arq/salarios.csv'
arq2 = pd.read_csv(file2)
print(arq2.head())
print("")
