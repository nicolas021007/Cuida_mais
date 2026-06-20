from typing import List
from domain.paciente import Paciente
from schemas.paciente import PacienteCreate, PacienteOut
from repositories.memory import Db


class PacienteService:

    def __init__(self, repo: Db):
        self.repo = repo
        

    def criar_paciente(self, data: PacienteCreate) -> PacienteOut:

        if self.repo.encontra_paciente_por_cpf(data.cpf):
            raise ValueError(f"Paciente com este CPF {data.cpf} já existe.")
        
        paciente = Paciente(
            cpf = data.cpf,
            nome = data.nome,
            data_nascimento = data.data_nascimento,
            sexo = data.sexo,
        )

        self.repo.save_paciente(paciente)
        return PacienteOut.model_validate(paciente)
    

    def listar_todos_pacientes(self) -> List[PacienteOut]:
        return [PacienteOut.model_validate(p) for p in self.repo.pacientes]
    
    def buscar_paciente_cpf(self, cpf: str) -> PacienteOut :
        paciente = self.repo.encontra_paciente_por_cpf(cpf)

        if not paciente:
            raise ValueError(f"Paciente com o CPF {cpf} não encontrado.")
        
        return PacienteOut.model_validate(paciente)
    
    def desativar_paciente(self,cpf: str) -> PacienteOut:

        paciente  = self.repo.encontra_paciente_por_cpf(cpf)

        if not paciente:
            raise ValueError(f"Paciente com o CPF {cpf} não encontrado.")
        
        paciente.ativo = False
        self.repo.save_paciente(paciente)

        return PacienteOut.model_validate(paciente)
    
    