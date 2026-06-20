from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import date, datetime
from models import Especialidade, Sexo


class DoutorCreate(BaseModel):

    nome: str
    email: EmailStr
    telefone: str
    data_nascimento: date
    sexo: Sexo
    especialidade: Especialidade

class DoutorOut(DoutorCreate):

    id: UUID
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        orm_mode = True
