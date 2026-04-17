#crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
#inteira
#ex digite um numero : 6.127 O numero 6.127 tem a parte inteira 6
import math
n = float((input('digite um numero Real: ')))
por = math.trunc(n)
print('A porção do seu numero e {}'.format(por))

