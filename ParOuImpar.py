from random import randint
vitorias = 0
escolha = 'S'
print('-='*10)
print('PAR OU ÍMPAR')
print('-='*10)
while escolha == 'S':
    jogadornumero = int(input('Escolha um número de 0 a 10: '))
    jogadorescolha = str(input('PAR OU ÍMPAR?[P/I] ')).upper().strip()
    numerocomputador = randint(0, 11)
    print(f'Eu escolhi o número {numerocomputador}')
    sorteio = numerocomputador + jogadornumero
    print(f'{jogadornumero} + {numerocomputador} = {sorteio}')
    if sorteio % 2 == 0:
        print(f'{sorteio} é PAR')
        if jogadorescolha == 'P':
            print('Você ganhou')
            print('-='*20)
            vitorias += 1
        else:
            print('Eu ganhei HAHAHA')
            print(f'Voce ganhou {vitorias} vezes')
            escolha = str(input('Vamos jogar denovo?[S/N] ')).upper().strip()
            vitorias = 0
            print('-=' * 20)
            if escolha == 'N':
                print('Finalizando o jogo...\n'
                      'Tchau!')
                break
    else:
        print(f'{sorteio} é IMPAR')
        if jogadorescolha == 'I':
            print('Você ganhou')
            print('-=' * 20)
            vitorias += 1
        else:
            print('Eu ganhei HAHAHA')
            print(f'Voce ganhou {vitorias} vezes')
            print('-=' * 20)
            vitorias = 0
            escolha = str(input('Vamos jogar denovo?[S/N] ')).upper().strip()
            print('-=' * 20)
            if escolha == 'N':
                print('-=' * 20)
                print('Finalizando o jogo...\n'
                      'Tchau!')
                break
