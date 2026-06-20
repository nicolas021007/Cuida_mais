from typing import List
from uuid import UUID
from domain.doutor import Doutor, Especialidade
from schemas.doutor import DoutorCreate, DoutorOut
from repositories.memory import Db



def _to_out(d: Doutor) -> DoutorOut:
    return DoutorOut(
        id= d.id,
        nome= d.nome,
        telefone=d.telefone,
        crm= d.crm, 
        especialidade=d.especialidade,
        ativo=d.ativo

    )
class DoutorService:

    def __init__(self, db: Db):
        self.repo = db

    """
    Tags:
    Cria um novo doutor com base nos dados fornecidos e o salva no repositório.

    Args:
    data (DoutorCreate): Os dados necessários para criar um novo doutor.

    Returns:
    DoutorOut: O objeto DoutorOut representando o doutor criado.
   
    """
    def criar_doutor(self, doutor_create: DoutorCreate) -> DoutorOut:
      doutor = Doutor(
          nome=doutor_create.nome,
          telefone=doutor_create.telefone,
          crm=doutor_create.crm,
          especialidade=doutor_create.especialidade,
          ativo=doutor_create.ativo
      )
      
      self.repo.save(doutor)
      return _to_out(doutor)
    

 
    def buscar_doutor(self,doutor_id:UUID)-> DoutorOut:
        """Tags:
        Busca um doutor pelo ID.

         Args:
            doutor_id (UUID): O ID do doutor a ser buscado.

        Returns:
            DoutorOut: O objeto DoutorOut representando o doutor encontrado.
    """
        
        doutor = self.repo.encontra_por_id(doutor_id)

        if not doutor:
            raise ValueError("Doutor não encontrado.")
        return _to_out(doutor)
    
   
    def listar_todos_doutores(self) -> List[DoutorOut]:
        """
    Tags:
    Lista todos os doutores cadastrados.


        returns:
        Uma lista de objetos DoutorOut representando os  doutores cadastrados.
    """
        doutores = self.repo.encontrar_todos_doutores()

        return [_to_out(d) for d in doutores]
    

    def listar_doutores_por_especialidade(self, especialidade: Especialidade) -> List[DoutorOut]:
        
        """
    Tags:
    Lista doutores por especialidade.  

    Args:
        especialidade (Especialidade): A especialidade para filtrar os doutores.

    Returns:
        Uma lista de objetos DoutorOut representando os doutores da especialidade especificada.
    """
        doutores = self.repo.encontrar_por_especialidade(especialidade)
        return [_to_out(d) for d in doutores]
   
    def desativar_doutor(self,doutor_id: UUID) -> DoutorOut:

         
        """
    Tags:
    Desativa um doutor pelo ID.

    Args:
        doutor_id (UUID): O ID do doutor a ser desativado.

    Returns:
        DoutorOut: O objeto DoutorOut representando o doutor desativado.
    """
        doutor = self.repo.encontra_por_id(doutor_id)

        if not doutor:
            raise ValueError("Doutor não encontrado.")
        
        doutor.desativar()
        self.repo.append(doutor)
        return _to_out(doutor)
    

    
    def ativar_doutor(self, doutor_id: UUID)-> DoutorOut:
        """
    Tags:
    Ativa um doutor pelo ID.

    Args:
        doutor_id (UUID): O ID do doutor a ser ativado.

    Returns:
        DoutorOut: O objeto DoutorOut representando o doutor ativado.
    """
        doutor = self.repo.find_by_id(doutor_id)

        if not doutor:
            raise ValueError("Doutor não encontrado.")
        
        doutor.ativar()
        self.repo.append(doutor)
        return _to_out(doutor)


    def  _get_or_raise(self,doutor_id: UUID)->Doutor:
        doutor = self.repo.encontra_por_id(doutor_id)   

        if not doutor:
            raise ValueError("Doutor não encontrado.")
        return doutor
    

    
    