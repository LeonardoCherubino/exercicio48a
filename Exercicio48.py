## Exercício 04-08: Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.

Num1 = int(input('Entre com o primeiro número. '))
Num2 = int(input('Entre com o segundo número. '))
Operacao = input('Entre com a operação desejada. +, -, *, /.  ')
# Resultado = 0

if Operacao == '+':
    Resultado = Num1 + Num2
elif Operacao == '-':
    Resultado = Num1 - Num2
elif Operacao == '*':
    Resultado = Num1 * Num2
elif Operacao == '/':
    Resultado = Num1 / Num2
else:
    print('Você escolheu opção inválida. ')
print('O resultado da operação escolhida é {}'.format(Resultado))    
