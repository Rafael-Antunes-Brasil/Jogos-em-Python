from time import sleep
from random import randint


def linha():
    print('-='*10)


vitpc = vitjog = empate = 0

print('Vamos jogar...')
sleep(1)
linha()
print('   JO  -  KEN  -  PÔ')
linha()
sleep(1)

while True:
    sleep(0.5)

    print('---Escolha---\n[1] Pedra\n[2] Papel\n[3] Tesoura')
    esc = int(input('Pedra, Papel ou Tesoura? '))
    maquina = randint(0, 2)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    linha()
    if esc == 1 and maquina == 0:
        empate += 1
        print('Pedra com Pedra\nEmpatamos')
    elif esc == 1 and maquina == 1:
        vitpc += 1
        print('Pedra pedre para Papel\nEu ganhei')
    elif esc == 1 and maquina == 2:
        vitjog += 1
        print('Pedra ganha de Tesoura\nVocê ganhou')
    elif esc == 2 and maquina == 0:
        vitjog += 1
        print('Papel ganha de Pedra\nVocê ganhou')
    elif esc == 2 and maquina == 1:
        empate += 1
        print('Papel com Papel\nEmpatamos')
    elif esc == 2 and maquina == 2:
        vitpc += 1
        print('Papel perde para Tesoura\nEu ganhei')
    elif esc == 3 and maquina == 0:
        vitpc += 1
        print('Tesoura perde para Pedra\nEu ganhei')
    elif esc == 3 and maquina == 1:
        vitjog += 1
        print('Tesoura ganha de Papel\nVocê ganhou')
    elif esc == 3 and maquina == 2:
        empate += 1
        print('Tesoura com Tesoura\nEmpatamos')
    linha()
    while True:
        esc = str(input('Quer continuar?[S/N] ')).upper().strip()
        if esc in 'SN':
            break
        print('\033[1;33mERRO! Digite S ou N\033[m')
    if esc in 'N':
        linha()
        break
jogadas = vitjog + vitpc + empate
print(f'Você ganhou {vitjog} vezes'
      f'\nEu ganhei {vitpc} vezes'
      f'\nEmpatamos {empate} vezes'
      f'\nForam {jogadas} jogadas')
print('Tchau =)')
