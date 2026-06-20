from pydantic import BaseModel
from datetime import date
from  domain.paciente import Sexo


"""
tag: paciente

Este módulo define os modelos de dados para a entidade "Paciente" usando a biblioteca Pydantic.   

- Paciente: Modelo principal que representa um paciente, contendo os campos nome, cpf, idade e sexo.
"""

class PacienteCreate(BaseModel):
    cpf: str
    nome: str
    data_nascimento: date
    sexo: Sexo
    
"""
tag: paciente

- PacienteOut: Modelo utilizado para retornar os dados de um paciente."""

class PacienteOut(BaseModel):
    cpf: str
    nome:str
    data_nascimento: date
    sexo: Sexo
    ativo: bool

    class Config:
        from_attributes = True