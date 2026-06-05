from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from domain.doutor import Especialidade
"""
Este módulo define os modelos de dados para a entidade Doutor usando a biblioteca Pydantic.

- Doutor: Modelo principal que representa um doutor, contendo os campos crm, nome , telefone , especialidade e se ele está ativo.
"""

class Doutor(BaseModel):
    crm: str = Field(min_length=7, max_length=10, description="CRM do doutor")
    nome: str = Field(min_length=3, max_length=100, description="Nome completo do doutor")
    telefone: str = Field(description="Número de telefone do doutor")
    especialidade: Especialidade = Field(description="Especialidade do doutor")
    ativo: bool = Field(default=True, description="Indica se o doutor está ativo")

"""
- DoutorCreate: Modelo utilizado para criar um novo doutor, contendo os mesmos campos do modelo Doutor.

"""

class DoutorCreate(BaseModel):
    crm: str= Field(min_length=7, max_length=9, description="CRM do doutor")
    nome:str = Field(min_length=3, max_length=100, description="Nome completo do doutor")
    telefone: str = Field(default =None, min_length=10, max_length=15, description="Número de telefone do doutor")
    especialidade: Especialidade = Field(default=None, description="Especialidade do doutor")
    ativo: bool = True

"""
- DoutorOut: Modelo utilizado para retornar os dados de um doutor.
"""
class DoutorOut(BaseModel):
    id: UUID
    crm: str
    nome:str
    telefone: str
    especialidade: Especialidade  
    ativo : bool = True

    class Config:
        orm_mode = True


