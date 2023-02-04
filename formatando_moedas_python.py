from dados import atividades

p = float(input('Digite um preço: '))
v = int(input('Digite um valor para ser calculado a porcentagem: '))
print(f'Um pessoa com {p}R$ de salário com aumento de {v} por cento passará a receber: {aumento(p, v, True)}')
print(f'Um pessoa com {p}R$ de salário com redução de {v} por cento passará a receber: {diminuir(p, v, True)}')
print(f'O dobro do valor R${p} é {dobro(p, True)}R$')
print(f'A metade de R${p} é {metade(p, True)}R$')
