"""
3- Descreva os principais operadores lógicos e condicionais:
"""

if __name__ == '__main__':
    """
    Operadores Lógicos: utilizados em Operações Booleanas, ou seja, fazem comparações entre valores True ou False. São 
    classificados em Operadores Binários (quando necessitam de dois Operandos) e Operador Unário (quando necessita de 
    apenas um Operando).
    
    Operadores Lógicos Binários:
        * Operador or - retorna True caso pelo menos uma de seus Operandos seja True, retorna False caso contrário.
        * Operador and - retorna True somente se ambos os Operandos forem True, retorna False caso contrário.
        
    Operador Lógico Unário
        * Operador not - inverte o valor lógico de seu Operando, ou seja, retorna True quando o operando é False e 
        retorna False quando o Operando é True
    """

    """
    Exemplo do Operador Binário or
    Exibe a mensagem de Bom dia se a idade for maior que 18 ou se o sexo for Feminino
    """
    nome = 'Carla'
    idade = 17
    sexo = 'F'
    if idade > 18 or sexo == 'F':
        print(f'Bom dia {nome}!')

    """
    Exemplo do Operador Binário and
    Exibe a mensagem de Bom dia se a idade for maior que 18 e se o sexo for Feminino
    """
    nome = 'Eduardo'
    idade = 17
    sexo = 'M'
    if idade > 18 and sexo == 'F':
        print(f'Bom dia {nome}!')  # Mensagem não será exibida

    """
    Exemplo do Operador Unário not
    Exibe a mensagem de Bom dia se o sexo não for Feminino
    """
    nome = 'Paulo'
    idade = 17
    sexo = 'M'
    if not sexo == 'F':
        print(f'Bom dia {nome}!')
