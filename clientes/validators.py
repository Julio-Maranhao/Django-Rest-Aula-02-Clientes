import re
from validate_docbr import CPF


def is_cpf_valid(cpf) -> bool:
    return CPF().validate(cpf)

def is_nome_valid(nome) -> bool:
    return nome.isalpha()
    
def is_rg_valid(rg) -> bool:
    return len(rg) == 9

def is_cell_number_valid(cell_number) -> bool:
    """Verifica se o celular é valido 00 91234-1234

    Args:
        cell_number (str): cell number

    Returns:
        bool: Cell number validator
    """
    resposta = re.findall('[0-9]{2} [0-9]{5}-[0-9]{4}', cell_number)
    return resposta