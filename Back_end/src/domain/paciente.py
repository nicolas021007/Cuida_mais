from dataclasses import dataclass
from datetime import date
from enum import Enum

"""
tag: paciente

Este módulo define a classe Paciente, que representa um paciente no sistema. A classe é decorada com @dataclass para facilitar a criação de instâncias e a manipulação dos dados.
"""

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    OUTRO = "Outro"
    NAO_INFORMADO ="Não informado"

@dataclass
class Paciente: 
    cpf: str
    nome: str
    sexo: Sexo
    data_nascimento: date
    ativo: bool = True
    