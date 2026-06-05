from dataclasses import dataclass,field
from uuid import UUID,uuid4
from enum import Enum

"""
Modelo de dados para representar um doutor.
"""

class Especialidade(str, Enum):
    Cardiologia = "cardiologia"
    Neurologia = "neurologia"
    Ortopedia = "ortopedia"
    Pediatria = "pediatria"



@dataclass

class Consultorio:
    cep: str
    logradouro: str 
    bairro: str
    cidade: str
    estado: str
    numero: str
    complemento: str = ""   
    
@dataclass

class Doutor:
   
    crm: str
    nome: str
    telefone: str
    email : str
    especialidade: Especialidade
    consultorio: Consultorio
    ativo: bool = True
    id: UUID = field(default_factory=uuid4)


    def __post_init__(self):
        if not (7<=len(self.crm)<= 9):
            raise ValueError("O CRM deve conter entre 7 e 9 caracteres.")
        
        if not self.nome:
            raise ValueError("O nome do doutor é obrigatorio.")
        
        if not self.telefone:
            raise ValueError("O telefone do doutor é obrigatorio.")
        
        if not self.especialidade:
            raise ValueError("A especialidade do doutor é obrigatoria.")
        

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    
    @property

    def esta_disponivel(self):
        return self.ativo
    

    def __str__(self):
        return f"Doutor CRM: {self.crm}, Nome: {self.nome}, Telefone: {self.telefone}, Especialidade: {self.especialidade}, Ativo: {self.ativo}"
      
