#Na matemática, quando multiplicamos um número decimal, a vírgula se desloca para a
#direita. E o número de casas que a vírgula desloca, é o número de zeros que tem 
#no divisor.
#Então, eu percorri a variável string 'num' para contar o número de 
#casas decimais. Pra assim, multiplicar o 'num' (que converti para float) por 10
#elevado ao número de casas decimais que o número tem. Assim, consegui transformar
#um número decimal, em um número inteiro, pra poder printar a representação
#fracionária desse número.

num = input(':')
decimal = False
cont = 0

#Transformando um número quebrado em um número inteiro
for a in num:
	if a == '.':
		decimal = True
		continue

	if decimal and a != '0':
		cont += 1

numint = float(num) * 10**cont

#Imprimindo a representação fracionária do número.
print(f'{int(numint)}/{10**cont}')
