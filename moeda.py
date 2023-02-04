def aumento(x, y, formato=False):
    """
    :param x: valor
    :param y: valor do aumento
    :return: retorna valor mais aumento digitado
    """
    res = x + (x * y) / 100
    return res if formato is False else real(res)


def diminuir(x, y, formato=False):
    """
    :param x: valor
    :param y: valor da reducao será calculado em porcetagem
    :return: retorna reducao no valor
    """
    res = x - (x * y) / 100
    return res if formato is False else real(res)

def dobro(num, formato=False):
    """
    :param num: numero a ser calculado
    :return: dobro do valor atribuido
    """
    res = num * 2
    return res if formato is False else real(res)

def metade(num, formato=False):
    """
    :param num: numero a ser calculado a metade
    :return: metade do valor
    """
    res = num / 2
    return res if formato is False else real(res)


def real(preco=0, dinheiro='R$'):
    return f'{dinheiro}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxa=0, taxa1=0):
    print('=' * 40)
    print(f'\033[1;33mRESUMO DE VALORES\033[m'.center(40))
    print('=' * 40)
    print(f'Preço analisado: \t{real(preco)}')
    print(f'Dobro do preço:  \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco), True}')
    print(f'{taxa}% de aumento: \t\{aumento(preco, taxa, True)}')
    print(f'{taxa1}% de redução: \t{diminuir(preco, taxa1, True)}')
    print('=' * 40)
