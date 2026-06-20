from typing import List
from fastapi import APIRouter, Depends,HTTPException
from repositories.memory import Db
from services.paciente import PacienteService
from schemas.paciente import PacienteCreate, PacienteOut


router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

db: Db = None

def set_db_pacientes(database: Db):
    global db
    db = database

def get_db_pacientes() ->Db:
    return db

def get_pacientes_service(database: Db = Depends(get_db_pacientes)) -> PacienteService:
    return PacienteService(database)

@router.post(
    "/",
    response_model=PacienteOut,
    status_code=201,
    summary="Criar um novo paciente"
)

def criar_paciente(data: PacienteCreate, service: PacienteService = Depends(get_pacientes_service)):

    try:
        return service.criar_paciente(data)
    except ValueError as e :
        raise HTTPException(status_code=400, detail= str(e))

@router.get(
    "/",
    response_model =List[PacienteOut],
    summary ="Listar todos os pacientes"
)

def listar_pacientes(service: PacienteService = Depends(get_pacientes_service)):
    return service.listar_todos_pacientes()


@router.get(
    "/paciente/{paciente_cpf}",
    response_model =PacienteOut,
    summary = "Obter detalhes de um paciente por CPF"

)

def buscar_paciente(paciente_cpf: str, service: PacienteService = Depends(get_pacientes_service)):

    try:
        return service.buscar_paciente_cpf(paciente_cpf)
    except ValueError as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.patch(
    "/paciente/{paciente_cpf}",
    response_model= PacienteOut,
    summary ="Desativar paciente por CPF"
)

def desativar_paciente_cpf(paciente_cpf: str, service: PacienteService = Depends(get_pacientes_service)):

    try:
        return service.desativar_paciente(paciente_cpf)
    except ValueError as e:
        raise HTTPException(status_code = 404, detail =str(e))
    
