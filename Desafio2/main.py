"""
2- Descreva as principais estruturas de repetição e explique cada uma delas:
"""

import re
from datetime import datetime

ANO_ATUAL = datetime.now().year
lista_clientes = [
    {
        'nome': 'André Pereira Silva',
        'data_nascimento': '01/05/1993',
        'sexo': 'M'
    },
    {
        'nome': 'Janína Pascoal Ramos',
        'data_nascimento': '02/04/1999',
        'sexo': 'F'
    },
    {
        'nome': 'Sabrina Santos Andrade',
        'data_nascimento': '26/08/1979',
        'sexo': 'F'
    },
    {
        'nome': 'João Gomes Sarter',
        'data_nascimento': '05/06/2000',
        'sexo': 'M'
    },
    {
        'nome': 'Fernanda Abreu Alves',
        'data_nascimento': '14/10/1995',
        'sexo': 'F'
    },
]

lista_clientes_copia = lista_clientes.copy()


def exibir_cliente(cliente) -> None:
    nome = cliente["nome"]
    data_nascimento = cliente["data_nascimento"]
    ano_nascimento = re.search(r"\d{4}", data_nascimento).group(0)
    sexo = cliente["sexo"]

    print(f'Nome: {nome}, Idade: {ANO_ATUAL - int(ano_nascimento)}, Sexo: {sexo}')


if __name__ == '__main__':
    """
    Estrutura de Repetição for: Utilizada quando se sabe a quantidade de iterações que se deve realizar em um loop. 

    Como exemplo, dada uma Lista de Clientes que contém Nome, Data de Nascimento e Sexo definida acima, podemos
    percorrer esta lista e exibir somente os dados dos 3 primeiros Clientes.
    """

    print('-' * 10, 'Exibindo os 3 primeiros Clientes da Lista', '-' * 10)
    for i in range(3):
        cliente = lista_clientes[i]  # Acessa um Cliente através do Índice da Lista
        exibir_cliente(cliente)

    """
    Estrutura de repetição while: utilizada quando não se sabe a quantidade de iterações que se deve realizar em um loop,
    podendo este ser executado indefinidamente ou até que uma determinada condição seja satisfeita. 

    Como exemplo, podemos utilizar a mesma Lista de Clientes, imaginando que não seja conhecida a quantidade de Clientes 
    presentes nesta lista. Podemos utilizar a Estrutura de Repetição while para remover cada Cliente do Início da Lista 
    até que esta fique vazia. 
    """
    print('\n', '-' * 10, 'Exibindo todos os Clientes da Lista', '-' * 10)
    while len(lista_clientes) > 0:
        cliente = lista_clientes.pop(0)  # Remove o Cliente do Início da Lista a cada Iteração
        exibir_cliente(cliente)

    """
    Estrutura de Repetição do while: utilizada quando se deseja que pelo menos uma repetição em um loop seja executada.

    No Python não existe esta estrutura, mas podemos simular seu comportamento através do seguinte exemplo: Mostrar o 
    primeiro Cliente do Sexo Feminino.
    """
    print('\n', '-' * 10, 'Exibindo o primeiro Cliente do Sexo Feminino da Lista de Clientes', '-' * 10)
    exibiu_cliente_feminino = False
    while not exibiu_cliente_feminino:
        cliente = lista_clientes_copia.pop(0)
        if cliente["sexo"] == 'F':
            exibir_cliente(cliente)
            exibiu_cliente_feminino = True
