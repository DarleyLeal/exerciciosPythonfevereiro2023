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
