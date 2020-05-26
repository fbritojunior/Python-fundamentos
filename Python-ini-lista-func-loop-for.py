# Testes iniciais com:
# Listas
# Variáveis 
# Operações matemáticas
# Funções Built-in
# Laços do tipo for 
# Laços condicionais if


# criando uma lista numérica
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Array:', arr)
type(arr)
print("")

# a partir uma lista numérica são impressos os valores pares
print('Valores pares: ')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in lista:
	if (val % 2 == 0): # verificando se o resto da divisão é igual a 0 
		print(val)
print("")

# criando uma terceira lista 
lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# usando loop for para varrer elementos da lista
# calcular o quadradado de cada item
# e realizar a soma dos elementos
soma = 0 # inicializando a variável soma 
for item in lista2:
	square = pow(item,2) # função pow = item**2
	soma += square
	print('%d' %square)
print('A soma dos valores é: %d.' %soma)
print("")

# criando uma lista com palavras
lista3 = ['Morango', "Banana", "Abacaxi", "Amora"]

# impressão da lista
print('Lista:', lista3)
print("")

# varrendo cada valor da lista e imprimindo usando loop for
size = len(lista3)
for item in range(0, size):
	print(lista3[item])
