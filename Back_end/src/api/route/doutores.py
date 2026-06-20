from  typing import  List
from fastapi import APIRouter,Depends, HTTPException
from uuid import UUID
from repositories.memory import Db
from services.doutor import DoutorService
from schemas.doutor import DoutorCreate, DoutorOut
from domain.doutor import Especialidade


router = APIRouter(prefix="/doutores", tags=["Doutores"])

db: Db = None

def set_db_doutores(database: Db):
    global db
    db = database

def get_db_doutores() -> Db:
    return db
"""
Este módulo define as rotas para a entidade Doutor, permitindo a criação e listagem de doutores.
"""
def get_doutor_service(database: Db = Depends(get_db_doutores))-> DoutorService:
    return DoutorService(database)


@router.post(
        "/", 
        response_model= DoutorOut,
        status_code=201,
        summary="Criar um novo doutor",
             )
def criar_doutor(data: DoutorCreate, service: DoutorService = Depends(get_doutor_service)):
    """
    Rota para criar um novo doutor.
    
    nome : nome completo do doutor
    crm : CRM do doutor
    telefone: número de telefone do doutor
    especialidade: especialidade do doutor
    ativo: indica se o doutor está ativo(opcional, padrão é True)

    """
    return service.criar_doutor(data)
    

@router.get(
    "/", 
    response_model=List[DoutorOut],
    summary="Listar todos os doutores"
)


def listar_doutores(service: DoutorService = Depends(get_doutor_service)):

    """
    Rota para listar todos os doutores cadastrados.
    """
    return service.listar_todos_doutores()


@router.get(
    "/{doutor_id}",
    response_model=DoutorOut,
    summary="Obter detalhes de um doutor por ID"
    )

def buscar_doutor(doutor_id: UUID, service: DoutorService = Depends(get_doutor_service)):
    
    """
    Rota para obter detalhes de um doutor específico usando seu ID.
    """
    try:
        return service.buscar_doutor(doutor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get(
    "/especialidade/{especialidade}",
    response_model=List[DoutorOut],
    summary="Listar doutores por especialidade"

)

def listar_doutores_por_especialidade(especialidade: Especialidade, service: DoutorService = Depends(get_doutor_service)):
    """
    Rota para listar doutores com base em sua especialidade
    """
    return service.listar_doutores_por_especialidade(especialidade)



@router.patch(
    "/{doutor_id}/desativar",
    response_model=DoutorOut,
    summary="Desativar um doutor por ID",

)

def desativar_doutor(doutor_id : UUID, service: DoutorService= Depends(get_doutor_service)):
    """
    Rotaa para desativar um doutor especificado por seu ID
    """

    try:
        return service.desativar_doutor(doutor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
