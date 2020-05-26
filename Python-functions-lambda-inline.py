# Construindo funções 
# Testes Iniciais
# função inline
# funçao Lambda
# funções built-in
# opera~ções matemáticas

# Primeira função: Olá, Mundo
# definição da função
def olaMundo():
	print('Hello, World!')

# chamando a função
olaMundo()
print("")

# Função para impressao de texto
# recebendo string como parâmetro
def primFunc(texto):
	print('Python é %s' %(texto)) # utilizando placeholder
	print("")

# chamando a função 
primFunc('poderosa!')

# função para quebra de palavras 
def split_string(text):
	return text.split(" ")


# definindo a cadeia de caracteres 
# e chamando a função
texto = "Isto é um teste"
print(split_string(texto)) # chamando a função e imprimindo
print("")

# Calculo do quadrado de um numero
# Definindo uma função inline
def potencia(num): return num ** 2

# Definindo uma função Lambda
square = lambda num: num ** 2

# definindo o valor
valor = 4

# chamando a função potencia e imprimindo 
print('Função inline:', potencia(valor))

# chamando a função lambda e imprimindo 
print('Função Lambda:', square(valor))

# Usando a função a built-in
print('Função Built-in:', pow(valor,2))
print("")


# Função para verificar se numero é par
par = lambda x: x % 2 == 0

# chamando a função e imprimindo
numero = 4
print('O número ' + str(numero) + ' é par?', par(numero))
print("")


# Criando uma função para somar dois números
addNum = lambda x,y: x + y 

# definindo valores, instanciando a função e imprimindo o resultado
valor1 = 3
valor2 = 5
soma = addNum(valor1, valor2)
print('O somatório de ' + str(valor1) + ' e ' + str(valor2) + ' é igual a', soma)
print("")
