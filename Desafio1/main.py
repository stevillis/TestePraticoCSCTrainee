"""
1- Desenvolver algoritmo para o problema:
- Ler a variável NOME;
- Enquanto o valor fornecido não for fornecido exibir mensagem de erro e solicitar
novamente a leitura;
- Quando o valor fornecido estiver correto, ler a variável SEXO;
- Ler a variável SEXO;
- Enquanto o valor fornecido não for correto (M,m,F,f) exibir mensagem de erro e
solicitar novamente a leitura;
- Quando o valor fornecido estiver correto, ler a variável ANO DE NASCIMENTO;
- Enquanto o valor fornecido não for fornecido exibir mensagem de erro e solicitar
novamente a leitura;
- Quando o valor fornecido estiver correto, escrever NOME, ANO DE NASCIMENTO,
IDADE e SEXO.
"""

from datetime import datetime

ANO_ATUAL = datetime.now().year


def is_nome_valido(nome) -> bool:
    """
    Valida o Nome.
    :param nome: Nome a ser validado.
    :return: True se o nome é composto por pelo menos 3 carqcteres não vazios e não númericos, False caso contrário.
    """
    return len(nome.strip()) >= 3 and not nome.isnumeric()


def is_sexo_valido(sexo) -> bool:
    """
    Valida o Sexo.
    :param sexo: Sexo a ser validado.
    :return: True se Sexo tiver um dos valores (M, m, F, f), False caso contrário.
    """
    return sexo.upper() in ['M', 'F']


def is_ano_valido(ano_nascimento) -> bool:
    """
    Valida o Ano de Nascimento.
    :param ano_nascimento: Ano a ser validado.
    :return: True se o Ano de Nascimento estiver entre 1900 e o Ano Atual, False caso contrário.
    """
    return 1900 <= ano_nascimento <= ANO_ATUAL


if __name__ == '__main__':
    msg_leia_nome = 'Forneça um valor para NOME: '
    msg_leia_sexo = 'Forneça um valor para SEXO: '
    msg_leia_ano_nascimento = 'Forneça um valor para ANO DE NASCIMENTO: '

    msg_erro_nome_invalido = 'NOME fornecido precisa ter pelo nenos 3 caracteres não vazios e não numéricos!\n'
    msg_erro_sexo_invalido = 'SEXO inválido! Informe um dos valores permitidos (M, m, F, f)\n'
    msg_erro_ano_invalido = f'Somente valores entre 1900 e {ANO_ATUAL} são aceitos!\n'

    NOME = input(msg_leia_nome)
    while not is_nome_valido(NOME):
        print(msg_erro_nome_invalido)
        NOME = input(msg_leia_nome)

    SEXO = input(msg_leia_sexo)
    while not is_sexo_valido(SEXO):
        print(msg_erro_sexo_invalido)
        SEXO = input(msg_leia_sexo)

    ANO_NASCIMENTO = 0
    while True:
        try:
            ANO_NASCIMENTO = int(input(msg_leia_ano_nascimento))
            if not is_ano_valido(ANO_NASCIMENTO):
                print(msg_erro_ano_invalido)
            else:
                break
        except ValueError:
            print(msg_erro_ano_invalido)

    print('\n', '-' * 25, 'DADOS INSERIDOS', '-' * 25)
    print(f'Nome: {NOME}, ANO DE NASCIMENTO: {ANO_NASCIMENTO}, IDADE: {ANO_ATUAL - ANO_NASCIMENTO}, SEXO: {SEXO}')
