#definindo os valores iniciais
num1 = 1 #num1 representa o número anterior da sequência.
num2 = 1 #num2 representa o número atual da sequência.

print('1\n1') # É a forma que eu encontrei de incluir o 1, 1 que tem na sequência.

for i in range(10):
	num2 = num1 + num2 #Somando os valores pra definir o próximo número da sequência.
	num1 = num2 - num1 #Subtraindo os valores para saber o número anterior da sequência.

	print(num2)

#Essa é a forma que eu encontrei de fazer a sequência de fibonacci.
