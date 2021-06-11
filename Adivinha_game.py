from random import randint
from time import sleep
r = str(input('Vamos jogar? [S/N]')).upper()
while r == 'S':
   print('-=-'*13)
   print('Estou pensando em um numero de 0 a 10...')
   print('-=-'*13)
   sleep(2)
   num = int(input('Em que numero pensei? '))
   n = randint(0, 10)
   palpites = 0
   while num != n:
       if num < n:
           print('Mais, tente novamente')
       else:
           print('Menos, tente novamente')
       num = int(input('Em que número eu pensei '))
       palpites += 1
   print('Você acertou eu pensei no numero {}'.format(n))
   print('Você precisou de {} palpites para acertar'.format(palpites))
   sleep(0.5)
   r = str(input('Jogar denovo?[S/N] ')).upper()