#Esse código na realidade é a re-construção que eu fiz de um outro código que eu achei na internet.

from random import choice

lista = ['abelha', 'macaco', 'matemática', 'livro', 'praia',
         'leão', 'celular', 'triângulo', 'história', 'capitalismo']
palavra_secreta = choice(lista)
dicas = {
     'abelha': 'Amarelo e preto',
     'macaco': 'Evolução humana',
     'matemática': 'Pesadelo de muitos na escola',
     'livro': 'conhecimento',
     'praia': 'Férias',
     'leão': 'Rei',
     'celular': 'Sem isso, sem vida',
     'triângulo': 'Forma ge...',
     'história': 'Passado',
     'capitalismo': 'Gera lixo e nos levará para a auto-destruição'
}

tutorialInicial = '''
Adivinhe a palavra!

Tente adivinhar a palavra (Regras) :
Se você pediu dica: 
Você terá 3 chances para adivinhar a palavra.
Se você não pediu dica :
Você terá 5 chances para adivinhar a palavra
'''

print(tutorialInicial)

dica = input(' Você vai querer uma dica ? ').lower()

if dica == 'sim':
    print(f'A sua dica é: {dicas[palavra_secreta]}. A palavra tem {len(palavra_secreta)} letras.') 

    for i in range(0, 3):
        palavra = input('->').lower()
        
        if palavra == palavra_secreta:
            print('Parabéns, você acertou!')
            break
        
        else:
            print('Você errou! Tente novamente.')

    else:
        print(f'Você perdeu. A palavra era {palavra_secreta}')

elif dica == 'não' or dica == 'nao':
    print(f'A sua dica é: {dicas[palavra_secreta]}. A palavra tem {len(palavra_secreta)} letras.') 

    for i in range(0, 5):
        palavra = input('->').lower()
        
        if palavra == palavra_secreta:
            print('Parabéns, você acertou!')
            break
        
        else:
            print('Você errou! Tente novamente.')

    else:
        print(f'Você perdeu. A palavra era {palavra_secreta}')
